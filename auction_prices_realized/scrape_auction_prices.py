#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import math
import pandas as pd
import requests

PAGE_MAX = 250
SCRAPE_URL = "https://www.psacard.com/auctionprices/GetItemLots"
EXAMPLE_URL = "https://www.psacard.com/auctionprices/baseball-cards/1967-topps/mets-rookies/values/187370"

class PsaAuctionPrices:
    def __init__(self, card_url):
        self.card_url = card_url
    
    def scrape(self):
        print("collecting data for {}".format(self.card_url))

        # Pull the card ID off the input url
        try:
            card_id = int(self.card_url.split("/")[-1])
        except:
            print("Input URL should end in a numeric value, it should look like this: {}".format(EXAMPLE_URL))
            return None
        
        # Get json data for input card
        sess = requests.Session()
        sess.mount("https://", requests.adapters.HTTPAdapter(max_retries=5))
        form_data = {
            "specID": str(card_id),
            "draw": 1,
            "start": 0,
            "length": PAGE_MAX
        }

        json_data = self.post_to_url(sess, form_data)
        sales = json_data["data"]

        # If there's more than PAGE_MAX sales results, keep calling the SCRAPE_URL until we have all of the sales
        # records
        total_sales = json_data["recordsTotal"]
        if total_sales > PAGE_MAX:
            additional_pages = math.ceil((total_sales - PAGE_MAX) / PAGE_MAX)
            for i in range(additional_pages):
                curr_page = i + 1
                form_data = {
                    "specID": str(card_id),
                    "draw": curr_page + 2,
                    "start": PAGE_MAX * curr_page,
                    "length": PAGE_MAX
                }

                json_data = self.post_to_url(sess, form_data)
                sales += json_data["data"]

        images = []
        a_urls = []
        prices = []
        dates = []
        grades = []
        quals = []
        lots = []
        a_houses = []
        sellers = []
        sale_types = []
        certs = []

        # Iterate over each sale, pull data elements from each sale
        for sale in sales:
            # Get image url
            images.append(self.get_image_url(sale))

            # Get auction url
            a_urls.append(self.get_auction_url(sale))

            # Get sales price
            prices.append(self.get_price(sale))

            # Get sale date
            dates.append(self.get_sale_date(sale))

            # Get grade
            grades.append(self.get_grade(sale))

            # Get qualifer
            quals.append(self.get_qualifier(sale))

            # Get lot number
            lots.append(self.get_lot_number(sale))

            # Get auction house
            a_houses.append(self.get_auction_house(sale))

            # Get seller
            sellers.append(self.get_seller_name(sale))

            # Get sale type (auction, BIN, Best Offer, etc)
            sale_types.append(self.get_sale_type(sale))

            # Get PSA certification number
            certs.append(self.get_psa_cert(sale))
        
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
            "lot_number": lots,
            "auction_url": a_urls,
            "img_url": images
        })
        
        # Write to csv
        df.to_csv(self.get_file_name(), index = False)

    def post_to_url(self, session, form_data):
        r = session.post(SCRAPE_URL, data=form_data)
        r.raise_for_status()
        json_data = r.json()
        time.sleep(3)
        return json_data

    def get_image_url(self, sale):
        if "ImageURL" in sale:
            return sale["ImageURL"]
        return math.nan

    def get_auction_url(self, sale):
        if "URL" in sale:
            return sale["URL"]
        return math.nan

    def get_price(self, sale):
        try:
            sale_price = sale["SalePrice"]
        except KeyError:
            return math.nan
        try:
            return float(sale_price.strip("$").replace(",", ""))
        except ValueError:
            print("Error: found malformed sales price value: {}\n" \
                  "For page {}".format(sale_price, self.card_url))
            return math.nan

    def get_sale_date(self, sale):
        if "EndDate" in sale:
            return sale["EndDate"]
        return math.nan

    def get_grade(self, sale):
        if "GradeString" in sale:
            return sale["GradeString"]
        return math.nan

    def get_qualifier(self, sale):
        if "HasQualifier" in sale:
            if bool(sale["HasQualifier"]):
                return sale["Qualifier"]
            return math.nan
        else:
            if sale["Qualifier"]:
                return sale["Qualifier"]
            return math.nan

    def get_lot_number(self, sale):
        if "LotNo" in sale:
            return sale["LotNo"]
        return math.nan

    def get_auction_house(self, sale):
        if "Name" in sale:
            return sale["Name"]
        return math.nan

    def get_seller_name(self, sale):
        if "AuctionName" in sale:
            return sale["AuctionName"]
        return math.nan

    def get_sale_type(self, sale):
        if "AuctionType" in sale:
            return sale["AuctionType"]
        return math.nan

    def get_psa_cert(self, sale):
        if "CertNo" in sale:
            return sale["CertNo"]
        return math.nan
    
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
