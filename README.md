# PSA Cards Web Scrapers

Collection of web scrapers for collecting data from [PSA Cards](https://www.psacard.com/). They are written using Python 3.

There is a web scraper for PSA [pop report](https://www.psacard.com/pop/) data, and PSA [auction prices realized](https://www.psacard.com/auctionprices/) 
data. Each subdirectory contains a README file with instructions on how to use, and what the data looks like. Each scraper 
writes its data to local file as CSV.

## Software Requirements

- [Python 3](https://www.python.org/downloads/)
- Python modules (these can be [PIP installed](https://datatofish.com/install-package-python-using-pip/))
  * [requests](https://2.python-requests.org/en/master/)
  * [cloudscraper](https://github.com/VeNoMouS/cloudscraper)
  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  * [html5lib](https://github.com/html5lib/html5lib-python)
  * [Pandas](https://pandas.pydata.org/)