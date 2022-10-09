# PSA Cards Pop Report Web Scraper

Web scraper for collecting data from the [pop report](https://www.psacard.com/pop/) database from the PSA website.
Built using Python.

**NOTE**: Neither of the scrapers are using Selenium. This Pop Report scraper was
using Selenium for about a year, but that's no longer needed, so to keep it as
user-friendly and simple as possible, it's just using the Requests library.

## Software Requirements

- [Python 3](https://www.python.org/downloads/)
- Python modules (these can be [PIP installed](https://datatofish.com/install-package-python-using-pip/))
  * [requests](https://2.python-requests.org/en/master/)
  * [Pandas](https://pandas.pydata.org/)

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
- Open Command Prompt / Terminal. CD to the directory that contains the `scrape_pop_report.py` file.
- Run `python scrape_pop_report.py`
  * NOTE: you may need to use `python3` in place of `python` in the command.
- The script will take 5-15 seconds per set to run, and will save a CSV file to `~/psa-scrape/pop_report/data` containing 
  all of the pop report data for the 2012 Prizm set.

You can add multiple PSA pop report urls to the `urls.txt` file, the code will iterate over them and save a CSV file for each url.

## Data

Here is an example of the data that is collected (2012 Prizm Basketball [here](https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837))

| SpecID  | SubjectName  | SortOrder | Variety     | CardNumber | CardNumberSort | GradeN0 | Grade1Q | Grade1 | Grade1_5Q | Grade1_5 | Grade2Q | Grade2 | Grade2_5 | Grade3Q | Grade3 | Grade3_5 | Grade4Q | Grade4 | Grade4_5 | Grade5Q | Grade5 | Grade5_5 | Grade6Q | Grade6 | Grade6_5 | Grade7Q | Grade7 | Grade7_5 | Grade8Q | Grade8 | Grade8_5 | Grade9Q | Grade9 | Grade10 | Total | GradeTotal | HalfGradeTotal | QualifiedGradeTotal |
|---------|--------------|-----------|-------------|------------|----------------|---------|---------|--------|-----------|----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|---------|--------|----------|---------|--------|---------|-------|------------|----------------|---------------------|
| 1946728 | LeBron James | 0.0       |             | 1          | 1              | 1       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 2      | 0        | 0       | 2      | 0        | 0       | 5      | 0        | 0       | 27     | 0        | 0       | 41     | 2        | 0       | 203    | 8        | 0       | 981    | 593     | 1865  | 1855       | 10             | 0                   |
| 1919849 | LeBron James | 0.0       | Green Prizm | 1          | 1              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 0        | 0       | 1      | 0        | 0       | 0      | 0        | 0       | 3      | 0        | 0       | 15     | 4       | 24    | 24         | 0              | 0                   |
| 1922912 | LeBron James | 0.0       | Prizm       | 1          | 1              | 1       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 2      | 0        | 0       | 3      | 0        | 0       | 1      | 0        | 0       | 11     | 0        | 0       | 41     | 30      | 89    | 89         | 0              | 0                   |
| 3404088 | Paul Pierce  | 0.0       |             | 2          | 2              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 0        | 0       | 7      | 0        | 0       | 65     | 80      | 153   | 153        | 0              | 0                   |
| 2523659 | Paul Pierce  | 0.0       | Gold Prizm  | 2          | 2              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 0        | 0       | 3      | 1       | 5     | 5          | 0              | 0                   |
| 3722709 | Paul Pierce  | 0.0       | Green Prizm | 2          | 2              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 2      | 0       | 2     | 2          | 0              | 0                   |
| 2700962 | Paul Pierce  | 0.0       | Prizm       | 2          | 2              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 0        | 0       | 24     | 9       | 34    | 34         | 0              | 0                   |
| 3853071 | Jrue Holiday | 0.0       |             | 3          | 3              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 0        | 0       | 17     | 24      | 42    | 42         | 0              | 0                   |
| 3851287 | Jrue Holiday | 0.0       | Gold Prizm  | 3          | 3              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 2       | 3     | 3          | 0              | 0                   |
| 4741027 | Jrue Holiday | 0.0       | Green Prizm | 3          | 3              | 0       | 0       | 0      | 0         | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 0      | 0        | 0       | 1      | 2       | 3     | 3          | 0              | 0                   |