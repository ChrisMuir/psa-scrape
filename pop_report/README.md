# PSA Cards Pop Report Web Scraper

Web scraper for collecting data from the [pop report](https://www.psacard.com/pop/) database from the PSA website.

## Usage

To get started, save the script file `scrape_pop_report.py` to your local computer.

Let's say we want to scrape pop report data for the 2012 Panini Prizm basketball set. The url for this set is
[https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837](https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837)

Here are the steps to take:

- Open `urls.txt`, add the correct `https://www.psacard.com/pop/` url to the list.
    - The format for the txt file should be the set name, followed by a single pipe (`|`), followed by the pop report url. 
    Here is an example:
    - `2012 Panini Prizm basketball | https://www.psacard.com/pop/basketball-cards/2012/panini-prizm/107837`
    - The "set name" doesn't necessarily need to match what PSA uses, it can be whatever you want it to be. The scrape will 
    use what you pass as the "set name" as part of the output file name.
- Open Command Prompt / Terminal. CD to the directory that contains the `scrape_pop_report.py` file.
- Run `python scrape_pop_report.py`
  * NOTE: you may need to use `python3` in place of `python` in the command.
- The script will take 6-7 seconds per set to run, and will save a CSV file to `~/psa-scrape/pop_report/data` containing 
all of the pop report data for the 2012 Prizm set.

You can add multiple PSA pop report urls to the `urls.txt` file, the code will iterate over them and save a CSV file for each url.

## Data

Here is an example of the data that is collected
```
df.head(n=5)
Out[1]: 
   card_number          name    variation  authentic  1  1_w_qualifiers  1.5  \
0            1  LeBron James          NaN          0  0               0    0   
1            1  LeBron James  Green Prizm          0  0               0    0   
2            1  LeBron James        Prizm          1  0               0    0   
3            2   Paul Pierce   Gold Prizm          0  0               0    0   
4            2   Paul Pierce        Prizm          0  0               0    0   
   1.5_w_qualifiers  2  2.5  2_w_qualifiers  3  3.5  3_w_qualifiers  4  4.5  \
0                 0  0    0               0  1    0               0  0    0   
1                 0  0    0               0  0    0               0  0    0   
2                 0  0    0               0  0    0               0  0    0   
3                 0  0    0               0  0    0               0  0    0   
4                 0  0    0               0  0    0               0  0    0   
   4_w_qualifiers  5  5.5  5_w_qualifiers  6  6.5  6_w_qualifiers   7  7.5  \
0               0  2    0               0  7    0               0  12    1   
1               0  0    0               0  1    0               0   0    0   
2               0  1    0               0  2    0               0   1    0   
3               0  0    0               0  0    0               0   0    0   
4               0  0    0               0  0    0               0   0    0   
   7_w_qualifiers   8  8.5  8_w_qualifiers    9  9_w_qualifiers   10  \
0               0  45    5               0  285               0  272   
1               0   2    0               0    9               0    4   
2               0   5    0               0   19               0   15   
3               0   0    0               0    2               0    0   
4               0   0    0               0    2               0    2   
   straight_grade_total  half_grade_total  qualifier_total  
0                   624                 6                0  
1                    16                 0                0  
2                    44                 0                0  
3                     2                 0                0  
4                     4                 0                0
```