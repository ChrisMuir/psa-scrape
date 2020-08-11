import os
import sys
import time
import math
import pandas as pd
import requests
from bs4 import BeautifulSoup

POP_URL_BASE = "https://www.psacard.com/pop/"

class PsaPopReport:
    def __init__(self, pop_url, set_name):
        self.pop_url = pop_url
        self.set_name = set_name

    def scrape(self):
        print("collecting data for {}".format(self.set_name))

        # Generate scrapable url
        try:
            scrape_url = self.gen_scrape_url()
        except ValueError as e:
            print(str(e))
            return

        # Get html data from input url
        sess = requests.Session()
        sess.mount("https://", requests.adapters.HTTPAdapter(max_retries=5))
        r = sess.get(scrape_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html5lib")
        time.sleep(5)
        all_data = [n for n in soup.find_all("tr")]

        # Get grade column headers
        self.grades = self.get_grades(all_data[0])

        # Loop over each "row" from the pop report, extract data from each row
        all_rows = []
        for elem in all_data:
            row = self.get_one_row(elem)
            if len(row) > 0:
                all_rows.append(row)

        # Create a dataframe and specify columns to write to file
        df = pd.DataFrame(all_rows)

        # Write to Excel file
        df.to_csv(self.get_file_name(), columns = all_rows[0].keys(), index=False)


    def gen_scrape_url(self):
        if POP_URL_BASE not in self.pop_url:
            raise ValueError("Input url must be a pop report url, must contain '{}', instead got: {}".format(POP_URL_BASE, self.pop_url))
        url_id = self.pop_url.split("/")[-1]
        scrape_url = "https://www.psacard.com/Pop/GetItemTable?headingID={}&categoryID=20003&isPSADNA=false".format(url_id)
        return scrape_url

    def get_grades(self, soup_element):
        try:
            grades = [n.contents[0].strip().lower() for n in soup_element.find_all("span")]
        except (IndexError, AttributeError, TypeError) as e:
            raise ValueError("Could not extract grades column headers, error: {}".format(str(e)))
        if "auth" not in grades:
            grades.insert(0, "authentic")
        return grades

    def get_one_row(self, soup_element):
        row = {}
        td = soup_element.find_all('td')

        if len(td) == 0 or "TOTAL POPULATION" in str(soup_element):
            return row

        # Find index of first set of pop info (grade Auth)
        idx = self.get_index_of_auth_grade(td)
        if idx == -1:
            return row

        # Get card number
        row["card_number"] = self.get_card_number(soup_element)

        # Get player name and card variation
        name, variation = self.get_name_and_card_variation(td)
        row["name"] = name
        row["variation"] = variation

        # Get the counts for each grade
        self.straight_grade_total = 0
        self.half_grade_total = 0
        self.qual_total = 0
        for grade in self.grades:
            # Get counts for the grade, and save them to the row dict
            try:
                counts = self.get_pop_counts_for_single_grade(td[idx])
            except (IndexError, AttributeError, TypeError) as e:
                print("Error getting pop counts for player {}, for grade {}, error: {}".format(name, grade, str(e)))
                counts = self.get_null_counts(grade)

            if len(counts) != 3:
                print("Expected 3 pop count ints, instead got {}, for player {}, for grade {}".format(counts, name, grade))
                counts = self.get_null_counts(grade)
                row = self.save_counts_to_row(counts, grade, row)
                idx += 1
                continue

            row = self.save_counts_to_row(counts, grade, row)
            idx += 1

        row["straight_grade_total"] = self.straight_grade_total
        row["half_grade_total"] = self.half_grade_total
        row["qualifier_total"] = self.qual_total

        return row

    def get_index_of_auth_grade(self, td_elements):
        # Searching for the ["Grade", "+", "Q"] element. Return the index after that one
        for idx, elem in enumerate(td_elements):
            try:
                if "grade" in [n.contents[0].lower() for n in elem.find_all("span")]:
                    return idx + 1
            except (IndexError, AttributeError, TypeError):
                return -1
        return -1

    def get_card_number(self, soup_element):
        num = soup_element.find("td", {'class': 'card-num'})
        try:
            return num.contents[0].strip()
        except (IndexError, AttributeError, TypeError):
            return math.nan

    def get_name_and_card_variation(self, td_elements):
        for elem in td_elements:
            strong_elem = elem.find("strong")
            if strong_elem:
                # Get player name
                try:
                    name = strong_elem.contents[0]
                except (IndexError, AttributeError, TypeError):
                    name = math.nan
                # Get card name/variation
                try:
                    card = str(elem).split("<br/>")[1].split("<span ")[0].strip()
                except (IndexError, AttributeError, TypeError):
                    card = math.nan
        return name, card

    def get_pop_counts_for_single_grade(self, td_elem):
        return [n.contents[0].strip() for n in td_elem.find_all("span")]

    def get_null_counts(self, grade):
        if grade == "authentic" or "10":
            return ["0", "-", "-"]
        if grade == "1" or "9":
            return ["0", "-", "0"]
        if grade == "1.5":
            return ["-", "0", "0"]
        return ["0"] * 3

    def save_counts_to_row(self, counts, grade, row):
        for idx, count in enumerate(counts):
            if count == "-":
                continue
            try:
                count = int(count)
            except ValueError:
                print("Unexpected non-int pop count value\nplayer: {}\ncard: {}\ncount: {}".format(row["name"], row["variation"], count))
            if idx == 0:
                row["{}".format(grade)] = count
                self.straight_grade_total += count
            elif idx == 1 and grade != "1.5":
                row["{}.5".format(grade)] = count
                self.half_grade_total += count
            elif idx == 1 and grade == "1.5":
                row["{}".format(grade)] = count
                self.half_grade_total += count
            elif idx == 2:
                row["{}_w_qualifiers".format(grade)] = count
                self.qual_total += count
        return row

    def get_file_name(self):
        f_name = "{}--{}".format(self.set_name.replace(" ", "-"), str(time.strftime("%Y-%m-%d-%H%M%S")))
        return "{}.csv".format(os.path.join("data", f_name))


if __name__ == '__main__':
    # Input validation
    try:
        input_url = [sys.argv[1]]
        if not input_url or not isinstance(input_url, str):
            raise ValueError("input must be a url string with base '{}'".format(POP_URL_BASE))
    except IndexError:
        # If no input url provided, read in urls from urls.txt
        if not os.path.exists("urls.txt"):
            raise ValueError("no input url passed and 'urls.txt' not found")
        with open("urls.txt") as f:
            urls_raw = [n for n in f.read().split("\n") if n]

    urls = {}
    for line in urls_raw:
        elems = [n.strip() for n in line.split("|")]
        # print("elems[0]: {}\nelems[1]: {}".format(elems[0], elems[1]))
        if len(elems) == 2:
            urls[elems[0]] = elems[1]
        elif len(elems) == 1:
            urls[elems[0]] = elems[0]
        else:
            raise ValueError("Malformed txt line:\n{}\nLines should be two pipe-separated elements, like this:\n"\
                             "2018 Topps Update baseball | https://www.psacard.com/pop/baseball-cards/2018/topps-update/161401")

    # If psa-scrape/data doesn't exist, create it
    if not os.path.exists("data"):
        os.makedirs("data")

    # Iterate over all urls
    for set_name, url in urls.items():
        # Initialize class and execute web scraping
        ppr = PsaPopReport(url, set_name)
        ppr.scrape()
