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
    
    def scrape(self):
        # Get html data from input url
        sess = requests.Session()
        sess.mount("https://", requests.adapters.HTTPAdapter(max_retries=5))
        r = sess.get(self.card_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html5lib")
        time.sleep(5)
        
        # Get image url links
        images = self.get_image_urls(soup)
        
        # Get sale prices
        prices = self.get_prices(soup)
        
        # Get dates of the sales
        dates = self.get_sale_dates(soup)
        
        # Get PSA grades and qualifiers
        grades, quals = self.get_grades(soup)
        
        # Get lot url links
        lots = self.get_lot_urls(soup)
        
        # Get auction houses
        a_houses = self.get_auction_houses(soup)
        
        # Get names of the sellers
        sellers = self.get_seller_names(soup)
        
        # Get sale types (auction, BIN, Best Offer, etc)
        sale_types = self.get_sale_types(soup)
        
        # Get PSA certification numbers
        certs = self.get_psa_certs(soup)
        
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
    
    
    def get_image_urls(self, soup):
        image_data = [n for n in soup.find_all("div", {'class': 'item-image'})]
        images = []
        for n in image_data:
            html = str(n)
            if "href" not in html:
                images.append(math.nan)
                continue
            images.append(html.split('href="')[1].split('"')[0])
        return images
    
    def get_prices(self, soup):
        prices = [float(n.string.strip("$").replace(",", "")) for n in soup.find_all("div", {'class': 'item item-price'})]
        return prices
    
    def get_sale_dates(self, soup):
        dates = [n.string for n in soup.find_all("div", {'class': 'item item-date'})]
        return dates
    
    def get_grades(self, soup):
        grade_data = soup.find_all("div", {'class': 'item item-grade'})
        grades = []
        quals = []
        for n in grade_data:
            html = str(n)
            grades.append(html.split("</span>")[1].split("<")[0].strip())
            if "<strong>" in html:
                quals.append(html.split("<strong>")[1].split("<")[0].strip())
            else:
                quals.append(math.nan)
        return grades, quals
    
    def get_lot_urls(self, soup):
        lot_data = soup.find_all("div", {'class': 'item item-lot'})
        base_url = "https://www.psacard.com"
        lots = []
        for n in lot_data:
            html = str(n)
            if "href" not in html:
                lots.append(math.nan)
                continue
            lots.append(base_url + html.split('href="')[1].split('"')[0])
        return lots
    
    def get_auction_houses(self, soup):
        a_houses = [n.string for n in soup.find_all("div", {'class': 'item item-auctionhouse'})]
        return a_houses
    
    def get_seller_names(self, soup):
        sellers = [n.string for n in soup.find_all("div", {'class': 'item item-auctionname'})]
        return sellers
    
    def get_sale_types(self, soup):
        sale_types = [n.string for n in soup.find_all("div", {'class': 'item item-auctiontype'})]
        return sale_types
    
    def get_psa_certs(self, soup):
        certs = [str(n).split("</span>")[1].split("<")[0] for n in soup.find_all("div", {'class': 'item item-cert'})]
        return certs
    
    def get_file_name(self):
        f_name = self.card_url.split("-cards/")[1].split("/values")[0].replace("/", "-")
        return "{}.csv".format(os.path.join("data", f_name))



if __name__ == '__main__':
    # Input validation
    input_url = sys.argv[1]
    if not input_url or not isinstance(input_url, str):
        raise ValueError("input must be a url string")
    
    # If psa-scrape/data doesn't exist, create it
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Initialize class and execute web scraping
    pap = PsaAuctionPrices(input_url)
    pap.scrape()





