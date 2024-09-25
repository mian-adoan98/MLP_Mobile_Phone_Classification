# scraping labels from orange mobile phone websites

import os 
import sys
import requests
from bs4 import BeautifulSoup
# from webscraping import webscraper_tool_man
from webscraper_tool_man import Webscraper, Images, Labels


# define the requirements for extracting labels from web data
orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443%2C5463%2C6203%2C5468%2C6196"
orange_response = requests.get(orange_url)


# create webscraper object --> check the status, create a parser
webscraper = Webscraper(orange_response)
orange_html = webscraper.check_status_request()
orange_soup = webscraper.create_parser(orange_html)

# print(orange_soup)

# create image object --> extract images from html page
all_images = orange_soup.find_all("img")
image_extractor = Images(all_images)
images_urls = image_extractor.extract_images(orange_url)
image_df = image_extractor.store_image_df(images_urls)

# create a labels object --> extract label from html page
all_labels = orange_soup.find_all("span")
label_extractor = Labels(all_labels)
print(all_labels)


# save the image data as a csv_file format
save_file = lambda filename, df: df.to_csv(filename)
save_file("image_data2.csv", image_df)

print(sys.path)

# ERROR : 
# 
# - TypeError: Images.store_image_df() takes 1 positional argument but 2 were given (line 28)
# #