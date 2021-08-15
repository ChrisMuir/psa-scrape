# PSA Cards Pop Report Web Scraper

Web scraper for collecting data from the [pop report](https://www.psacard.com/pop/) database from the PSA website.
Built using Python and Selenium.

## Software Requirements

- [Python 3](https://www.python.org/downloads/)
- Python modules (these can be [PIP installed](https://datatofish.com/install-package-python-using-pip/))
  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * [html5lib](https://github.com/html5lib/html5lib-python)
  * [Pandas](https://pandas.pydata.org/)
  * [Selenium](https://selenium-python.readthedocs.io/installation.html)

This scraper uses Selenium and ChromeDriver to pull pop report HTML. To use it, you must download ChromeDriver. 
Notes on ChromeDriver:
- Download page [here](https://chromedriver.chromium.org/downloads)
- Quick tutorial on web scraping in Python with Selenium and ChromeDriver [here](https://towardsdatascience.com/how-to-use-selenium-to-web-scrape-with-example-80f9b23a843a)
- You must edit the line `CHROMEDRIVER_PATH = "/path/to/local/chromedriver"` at the top of the file 
`scrape_pop_report.py`, to point to your locally downloaded ChromeDriver executable file.

## Usage

To get started, save the directory `pop_report` to your local computer.

Let's say we want to scrape pop report data for the 2012 Panini Prizm basketball set. The url for this set is
[https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837](https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837)

Here are the steps to take:

- Open `urls.txt`, add the correct `https://www.psacard.com/pop/` url to the list.
    - The format for the txt file should be the set name, followed by a single pipe (`|`), followed by the pop report url. 
    Here is an example:
    - `2012 Panini Prizm basketball | https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837`
    - The "set name" doesn't necessarily need to match what PSA uses, it can be whatever you want it to be. The scraper will 
    use what you pass as the "set name" as part of the output file name.
- Open `scrape_pop_report.py`, edit the line `CHROMEDRIVER_PATH = "/path/to/local/chromedriver"` at 
  the top of the file to point to your locally downloaded ChromeDriver executable file.
- Open Command Prompt / Terminal. CD to the directory that contains the `scrape_pop_report.py` file.
- Run `python scrape_pop_report.py`
  * NOTE: you may need to use `python3` in place of `python` in the command.
- You should see a new Google Chrome window open, and start automatically navigating to the PSA pages that contain the 
  pop report data.
- The script will take 5-15 seconds per set to run, and will save a CSV file to `~/psa-scrape/pop_report/data` containing 
  all of the pop report data for the 2012 Prizm set.

You can add multiple PSA pop report urls to the `urls.txt` file, the code will iterate over them and save a CSV file for each url.

## Data

Here is an example of the data that is collected (2012 Prizm Basketball [here](https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837))

| card_number | name          | variation   | auth | 1 | 1_w_qualifiers | 1.5 | 1.5_w_qualifiers | 2 | 2.5 | 2_w_qualifiers | 3 | 3.5 | 3_w_qualifiers | 4 | 4.5 | 4_w_qualifiers | 5 | 5.5 | 5_w_qualifiers | 6  | 6.5 | 6_w_qualifiers | 7  | 7.5 | 7_w_qualifiers | 8  | 8.5 | 8_w_qualifiers | 9   | 9_w_qualifiers | 10  | straight_grade_total | half_grade_total | qualifier_total |
|-------------|---------------|-------------|------|---|----------------|-----|------------------|---|-----|----------------|---|-----|----------------|---|-----|----------------|---|-----|----------------|----|-----|----------------|----|-----|----------------|----|-----|----------------|-----|----------------|-----|----------------------|------------------|-----------------|
| 1           | LeBron James  |             | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 1 | 0   | 0              | 1 | 0   | 0              | 3 | 0   | 0              | 13 | 0   | 0              | 20 | 1   | 0              | 81 | 6   | 0              | 511 | 0              | 369 | 999                  | 7                | 0               |
| 1           | LeBron James  | Green Prizm | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 1 | 0   | 0              | 1  | 0   | 0              | 0  | 0   | 0              | 2  | 0   | 0              | 10  | 0              | 4   | 18                   | 0                | 0               |
| 1           | LeBron James  | Prizm       | 1    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 2 | 0   | 0              | 2  | 0   | 0              | 1  | 0   | 0              | 8  | 0   | 0              | 29  | 0              | 21  | 64                   | 0                | 0               |
| 2           | Paul Pierce   |             | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 4  | 0   | 0              | 9   | 0              | 23  | 36                   | 0                | 0               |
| 2           | Paul Pierce   | Gold Prizm  | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 2   | 0              | 0   | 2                    | 0                | 0               |
| 2           | Paul Pierce   | Prizm       | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 1  | 0   | 0              | 3   | 0              | 2   | 6                    | 0                | 0               |
| 3           | Jrue Holiday  | Gold Prizm  | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 1   | 0              | 0   | 1                    | 0                | 0               |
| 3           | Jrue Holiday  | Prizm       | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 2   | 0              | 2   | 4                    | 0                | 0               |
| 4           | Dwight Howard |             | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0   | 0              | 3   | 3                    | 0                | 0               |
| 4           | Dwight Howard | Prizm       | 0    | 0 | 0              | 0   | 0                | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0 | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 0  | 0   | 0              | 4   | 0              | 0   | 4                    | 0                | 0               |