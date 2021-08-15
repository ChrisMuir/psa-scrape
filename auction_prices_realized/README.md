# PSA Cards Auction Prices Realized Web Scraper

Web scraper for collecting data from the [auction prices realized](https://www.psacard.com/auctionprices/) database 
from the PSA website.

## Software Requirements

- [Python 3](https://www.python.org/downloads/)
- Python modules (these can be [PIP installed](https://datatofish.com/install-package-python-using-pip/))
  * [requests](https://2.python-requests.org/en/master/)
  * [Pandas](https://pandas.pydata.org/)

## Usage

To get started, save the script file `scrape_auction_prices.py` to your local computer.

Let's say we want to scrape sales history data on the 1972 Topps Roberto Clemente card #309. The url for this card is 
[https://www.psacard.com/auctionprices/baseball-cards/1972-topps/roberto-clemente/values/190786](https://www.psacard.com/auctionprices/baseball-cards/1972-topps/roberto-clemente/values/190786)

Here are the steps to take:

- Open `urls.txt`, add the correct `https://www.psacard.com/auctionprices/` url to the list.
- Open Command Prompt / Terminal. CD to the directory that contains the `scrape_auction_prices.py` file.
- Run `python scrape_auction_prices.py`
  * NOTE: you may need to use `python3` in place of `python` in the command.
- The script will save a CSV file to `~/psa-scrape/auction_prices_realized/data`
  containing all of the sales data on the 1972 Topps Clemente card.
- The script run-time will depend on how many sales there are per card. It will take about 
  4-5 seconds per 250 sales to run.

You can add multiple PSA auction price urls to the `urls.txt` file, the code will iterate over them and save a CSV file for each url.

## Data

Here is an example of the data that is collected (Tom Seaver rookie [here](https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/values/187370))

| date      | grade | qualifier | price   | auction_house          | seller                                             | sale_type | psa_certification | lot_number   | auction_url                                                                                                                                                          | img_url                                                                                                  | 
|-----------|-------|-----------|---------|------------------------|----------------------------------------------------|-----------|-------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------| 
| 8/12/2021 | 7     |           | 1744.14 | Mile High Card Company | July/August 2021 Auction                           | Auction   | 04358855          | 526          | http://milehighcardco.com/1967_Topps__581_Mets_Rookie_Stars_Bill_Denehy_Tom_-LOT78319.aspx                                                                           | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/2151671213759425378/-7777829671369309491/images/1.jpg | 
| 8/12/2021 | 8     |           | 4974.0  | Mile High Card Company | July/August 2021 Auction                           | Auction   | 04002835          | 369          | http://milehighcardco.com/1967_Topps__581_Mets_Rookie_Stars_Tom_Seaver_PSA_8-LOT77887.aspx                                                                           | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/2151671213759425378/8952858551136403460/images/1.jpg  | 
| 8/11/2021 | 6     |           | 1476.0  | Goldin Auctions        | Summer Premium Card and Memorabilia Auction Closin | Auction   | 11675193          | 1184         | https://goldinauctions.com/LotDetail.aspx?inventoryid=99602                                                                                                          | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/6244593983304884209/-419715309701125055/images/1.jpg  | 
| 8/11/2021 | 7     |           | 1722.0  | Goldin Auctions        | Summer Premium Card and Memorabilia Auction Closin | Auction   | 45089689          | 1182         | https://goldinauctions.com/LotDetail.aspx?inventoryid=100875                                                                                                         | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/6244593983304884209/-5435840970924731443/images/1.jpg | 
| 8/11/2021 | 7     |           | 1722.0  | Goldin Auctions        | Summer Premium Card and Memorabilia Auction Closin | Auction   | 01076426          | 1183         | https://goldinauctions.com/LotDetail.aspx?inventoryid=98512                                                                                                          | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/6244593983304884209/8928093638758707516/images/1.jpg  | 
| 8/9/2021  | 8     |           | 4091.41 | eBay                   | kfinnerty2010                                      | Auction   | 42276539          | 164969734267 | https://www.ebay.com/itm/164969734267                                                                                                                                | https://d1w8cc2yygc27j.cloudfront.net/4315666646273767532/5984903745470514110.jpg                        | 
| 7/26/2021 | 8     |           | 3840.0  | Heritage Auctions      | Summer Sports Card Catalog Auction                 | Auction   | 09063818          | 53856        | https://sports.ha.com/itm/baseball/1967-topps-tom-seaver-mets-rookies-581-psa-nm-mt-8/a/50043-53856.s?ic4=GalleryView-ShortDescription-071515                        | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/5868395477352266266/-2182864976459381753/images/1.jpg | 
| 7/26/2021 | 9     |           | 22800.0 | Heritage Auctions      | Summer Sports Card Catalog Auction                 | Auction   | 30600839          | 53857        | https://sports.ha.com/itm/baseball/1967-topps-tom-seaver-mets-rookie-stars-581-psa-mint-9-only-three-higher-/a/50043-53857.s?ic4=GalleryView-ShortDescription-071515 | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/5868395477352266266/-8420421931069035068/images/1.jpg | 
| 7/21/2021 | 8     |           | 5300.0  | eBay                   | the-vintage-vine                                   | Auction   | 56808823          | 203527556618 | https://www.ebay.com/itm/203527556618                                                                                                                                | https://d1w8cc2yygc27j.cloudfront.net/519044342852525966/-3407617017172855156.jpg                        | 
| 7/20/2021 | 8     | OC        | 1107.0  | Mile High Card Company | Extra Innings July 2021                            | Auction   | 16464967          | 441          | http://milehighcardco.com/1967_Topps_Mets_Rookies__581_B__Denehy__T__Seaver_-LOT78953.aspx                                                                           | https://s3-us-west-2.amazonaws.com/cu-apr/auctions/-5520704063189957233/5685845152198563800/images/1.jpg | 

