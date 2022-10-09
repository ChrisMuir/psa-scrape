# PSA Cards Web Scrapers

Collection of web scrapers for collecting data from [PSA Cards](https://www.psacard.com/). They are written using Python 3.

There is a web scraper for PSA [pop report](https://www.psacard.com/pop/) data, and PSA [auction prices realized](https://www.psacard.com/auctionprices/) 
data. Each subdirectory contains a README file with instructions on how to use, and what the data looks like. Each scraper 
writes its data to local file as CSV.

**NOTE**: Neither of the scrapers are using Selenium. The Pop Report scraper was
using Selenium for about a year, but that's no longer needed, so to keep it as 
user-friendly and simple as possible, it's just using the Requests library.