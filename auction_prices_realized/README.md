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

Here is an example of the data that is collected (Tom Seaver rookie [here](https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/values/187370))

| date       | grade | qualifier | price   | auction_house   | seller                                      | sale_type  | psa_certification | img_url                                                                                                  | lot_url                                                                                      |
|------------|-------|-----------|---------|-----------------|---------------------------------------------|------------|-------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| 11/3/2020  | 9     | (OC)      | 2751    | eBay            | probstein123                                | Auction    | 15043229          | https://d1w8cc2yygc27j.cloudfront.net/3997047096083378937/-3963029703506628300.jpg                       | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4625316 |
| 11/1/2020  | 4     |           | 738     | Goldin Auctions | 2020 October Legends Closing Oct 31 & Nov 1 | Auction    | 8239144           | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/5444725223786918352/-7038209808390560069/images/1.jpg | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4626652 |
| 10/29/2020 | 6     |           | 1250    | eBay            | pwcc_auctions                               | Auction    | 26305299          | https://d1w8cc2yygc27j.cloudfront.net/-9082362744966253473/-8286543740984330547.jpg                      | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4594443 |
| 10/29/2020 | 7     |           | 1433    | eBay            | vntgbill176r                                | Auction    | 28146152          | https://d1w8cc2yygc27j.cloudfront.net/6219505144886152599/7651558168319032332.jpg                        | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4603057 |
| 10/28/2020 | 4     |           | 865     | eBay            | krakow1                                     | Best Offer | 50863218          | https://d1w8cc2yygc27j.cloudfront.net/3152591494732217471/-8657090745106659523.jpg                       | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4655334 |
| 10/21/2020 | 5     |           | 1400    | eBay            | jets2125                                    | Auction    | 48924870          | https://d1w8cc2yygc27j.cloudfront.net/-1319572707719838756/8583382082606840294.jpg                       | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4589297 |
| 10/15/2020 | 8     |           | 3451    | eBay            | pwcc_auctions                               | Auction    | 42276540          | https://d1w8cc2yygc27j.cloudfront.net/4086745062401735465/1598908627707579003.jpg                        | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4530555 |
| 10/5/2020  | 7     |           | 1774.99 | eBay            | vintagerookies                              | Best Offer | 2103877           | https://d1w8cc2yygc27j.cloudfront.net/-7754476056703969743/6231932511335009200.jpg                       | https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/auction/4517605 |