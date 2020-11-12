#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import math
import pandas as pd
import requests
from bs4 import BeautifulSoup


class PsaAuctionPrices:
    def __init__(self, card_url):
        self.card_url = card_url
        self.base_url = "https://www.psacard.com"
    
    def scrape(self):
        print("collecting data for {}".format(self.card_url))
        
        # Get html data from input url
        sess = requests.Session()
        sess.mount("https://", requests.adapters.HTTPAdapter(max_retries=5))
        r = sess.get(self.card_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html5lib")
        time.sleep(5)

        images = []
        prices = []
        dates = []
        grades = []
        quals = []
        lots = []
        a_houses = []
        sellers = []
        sale_types = []
        certs = []

        trs = soup.find_all(lambda tag: tag.name == "tr" and "data-hasqualifier" in tag.attrs)

        for tr in trs:
            tds = tr.find_all("td")

            # Get image url
            images.append(self.get_image_url(tds))

            # Get sales price
            prices.append(self.get_price(tds))

            # Get sale date
            dates.append(self.get_sale_date(tds))

            # Get grade and qualifer
            grade, qual = self.get_grade_and_qualifier(tds)
            grades.append(grade)
            quals.append(qual)

            # Get lot url
            lots.append(self.get_lot_url(tds))

            # Get auction house
            a_houses.append(self.get_auction_house(tds))

            # Get seller
            sellers.append(self.get_seller_name(tds))

            # Get sale type (auction, BIN, Best Offer, etc)
            sale_types.append(self.get_sale_type(tds))

            # Get PSA certification number
            certs.append(self.get_psa_cert(tds))
        
        # Create a dataframe
        df = pd.DataFrame({
            "date": dates, 
            "grade": grades, 
            "qualifier": quals, 
            "price": prices, 
            "auction_house": a_houses, 
            "seller": sellers, 
            "sale_type": sale_types, 
            "psa_certification": certs, 
            "img_url": images, 
            "lot_url": lots
        })
        
        # Write to Excel file
        df.to_csv(self.get_file_name(), index = False)

    def get_image_url(self, td_elements):
        for elem in td_elements:
            a_tag = elem.find("a", href=True)
            if a_tag and "auctionprices" not in a_tag["href"]:
                return a_tag["href"]
        return math.nan

    def get_price(self, td_elements):
        for td in td_elements:
            if td.has_attr("data-saleprice"):
                try:
                    return float(td.string.strip("$").replace(",", ""))
                except ValueError:
                    print("Error: found malformed sales price value: {}\n"\
                          "For page {}".format(td.string, self.card_url))
                    return math.nan
        return math.nan

    def get_sale_date(self, td_elements):
        for td in td_elements:
            if td.has_attr("data-saledate"):
                return td.string
        return math.nan

    def get_grade_and_qualifier(self, td_elements):
        grade = math.nan
        qual = math.nan
        grade_elem = None
        for td in td_elements:
            if td.has_attr("data-order") and td.has_attr("data-search"):
                grade_elem = td
                break
        if grade_elem:
            grade = grade_elem.get_text().strip().split(" ")[0]
            if grade_elem.find("strong"):
                qual = grade_elem.find("strong").string
        if not grade and "psadna" in str(grade_elem).lower():
            grade = "psadna"
        if "authentic altered" in str(grade_elem).lower():
            grade = "authentic altered"
        return grade, qual

    def get_lot_url(self, td_elements):
        for idx, td in enumerate(td_elements):
            if td.has_attr("class") and td.has_attr("data-order") and td.find("a", href=True):
                return self.base_url + td.find("a")["href"]
        return math.nan

    def get_auction_house(self, td_elements):
        idx = self.lookup_by_index_offset(td_elements, 1)
        if idx == -1:
            return math.nan
        return td_elements[idx].string

    def get_seller_name(self, td_elements):
        idx = self.lookup_by_index_offset(td_elements, 2)
        if idx == -1:
            return math.nan
        return td_elements[idx].string

    def get_sale_type(self, td_elements):
        idx = self.lookup_by_index_offset(td_elements, 3)
        if idx == -1:
            return math.nan
        return td_elements[idx].string

    def get_psa_cert(self, td_elements):
        idx = self.lookup_by_index_offset(td_elements, 4)
        if idx == -1:
            return math.nan
        return td_elements[idx].string

    def lookup_by_index_offset(self, td_elements, offset):
        for idx, td in enumerate(td_elements):
            if td.has_attr("class") and td.has_attr("data-order") and td.find("a", href=True):
                return idx + offset
        return -1
    
    def get_file_name(self):
        f_name = self.card_url.split("-cards/")[1].split("/values")[0].replace("/", "-")
        return "{}.csv".format(os.path.join("data", f_name))



if __name__ == '__main__':
    # Input validation
    try:
        input_url = [sys.argv[1]]
        if not input_url or not isinstance(input_url, str):
            raise ValueError("input must be a url string with base 'https://www.psacard.com/auctionprices/'")
    except IndexError:
        # If no input url provided, read in urls from urls.txt
        if not os.path.exists("urls.txt"):
            raise ValueError("no input url passed and 'urls.txt' not found")
        with open("urls.txt") as f:
            urls = [n for n in f.read().split("\n") if n]

    # If psa-scrape/data doesn't exist, create it
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Iterate over all urls
    for url in urls:
        # Initialize class and execute web scraping
        pap = PsaAuctionPrices(url)
        pap.scrape()
