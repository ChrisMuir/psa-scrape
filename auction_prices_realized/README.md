# PSA Cards Auction Prices Realized Web Scraper

Web scraper for collecting data from the [auction prices realized](https://www.psacard.com/auctionprices/) database 
from the PSA website.

## Usage

To get started, save the script file `scrape_auction_prices.py` to your local computer.

Let's say we want to scrape sales history data on the 1972 Topps Roberto Clemente card #309. The url for this card is 
[https://www.psacard.com/auctionprices/baseball-cards/1972-topps/roberto-clemente/values/190786](https://www.psacard.com/auctionprices/baseball-cards/1972-topps/roberto-clemente/values/190786)

Here are the steps to take:

- Open `urls.txt`, add the correct `https://www.psacard.com/auctionprices/` url to the list.
- Open Command Prompt / Terminal. CD to the directory that contains the `scrape_auction_prices.py` file.
- Run `python scrape_auction_prices.py`
  * NOTE: you may need to use `python3` in place of `python` in the command.
- The script will take 6-7 seconds per card to run, and will save a CSV file to `~/psa-scrape/auction_prices_realized/data` 
containing all of the sales data on the 1972 Topps Clemente card.

You can add multiple PSA auction price urls to the `urls.txt` file, the code will iterate over them and save a CSV file for each url.

## Data

Here is an example of the data that is collected
```
df.head(n=5)
Out[1]: 
        date grade qualifier   price auction_house        seller sale_type  \
0  6/27/2019   8.5       NaN  176.51          eBay  probstein123   Auction   
1  6/27/2019     4       NaN   21.23          eBay  probstein123   Auction   
2  6/26/2019     9       NaN  412.00          eBay  probstein123   Auction   
3  6/25/2019     8       NaN  155.49          eBay  probstein123   Auction   
4  6/25/2019     3       NaN   16.50          eBay  probstein123   Auction   

  psa_certification                                            img_url  \
0          42333836  https://d1w8cc2yygc27j.cloudfront.net/-4937118...   
1          42333835  https://d1w8cc2yygc27j.cloudfront.net/-6804739...   
2          20230681  https://d1w8cc2yygc27j.cloudfront.net/-3373097...   
3          42132794  https://d1w8cc2yygc27j.cloudfront.net/40566575...   
4          43468148  https://d1w8cc2yygc27j.cloudfront.net/-9351353...   

                                             lot_url  
0  https://www.psacard.com/auctionprices/baseball...  
1  https://www.psacard.com/auctionprices/baseball...  
2  https://www.psacard.com/auctionprices/baseball...  
3  https://www.psacard.com/auctionprices/baseball...  
4  https://www.psacard.com/auctionprices/baseball...  
```