# scraping labels from orange mobile phone websites

import os 
import sys
import requests
from bs4 import BeautifulSoup
# from webscraping import webscraper_tool_man
from webscraper_tool_man import Webscraper, Images, Labels

# urls cosntants
orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443%2C5463%2C6203%2C5468%2C6196"
amazon_url = "https://www.amazon.com.be/-/en/s?i=electronics&rh=n%3A27862520031%2Cp_123%3A110955%7C146762%7C329744%7C338933%7C46655&dc&fs=true&language=en&qid=1728339313&rnid=91049096031&ref=sr_nr_p_123_5&ds=v1%3AgO9ITbY27GiGtlO5Y0Ky%2BeW1wIFpSXrWqeL5%2BaZ024k"

# ## Orange_url --- --------------------------------------------------------------------------------------------------------------
# # define the requirements for extracting labels from web data
# orange_response = requests.get(orange_url)

# # create webscraper object --> check the status, create a parser
orange_scraper = Webscraper(orange_response)
# # orange website
# orange_html = amazon_scraper.check_status_request()
# amazon_soup = amazon_scraper.create_parser(orange_html)

# # print(amazon_soup)

# # create image object --> extract images from html page
# all_images = amazon_soup.find_all("img")
# image_extractor = Images(all_images)
# images_urls = image_extractor.extract_images(orange_url)
# image_df = image_extractor.store_image_df(images_urls)

# # create a labels object --> extract label from html page
# all_labels = amazon_soup.find_all("span")
# label_extractor = Labels(all_labels)
# print(all_labels)


# # save the image data as a csv_file format
# save_file = lambda filename, df: df.to_csv(filename)
# save_file("image_data2.csv", image_df)

# print(sys.path)

## Amazon -------------------------------------------------------------------------------------------------------------------
# define a webscraper object + create response --> extract data from aamazon website
amazon_response = requests.get(amazon_url)

# create webscraper object --> check the status, create a parser
amazon_scraper = Webscraper(amazon_response)
# orange website
amazon_html = amazon_scraper.check_status_request()
amazon_soup = amazon_scraper.create_parser(amazon_html)

# amazon website
amazon_html = amazon_scraper.check_status_request()
print(amazon_html)

# print(amazon_soup)

# create image object --> extract images from html page
all_images = amazon_soup.find_all("img")
image_extractor = Images(all_images)
images_urls = image_extractor.extract_images(orange_url)
image_df = image_extractor.store_image_df(images_urls)

# create a labels object --> extract label from html page
all_labels = amazon_soup.find_all("span")
label_extractor = Labels(all_labels)
print(all_labels)

# save the image data as a csv_file format
save_file = lambda filename, df: df.to_csv(filename)
save_file("image_data2.csv", image_df)

print(sys.path)


# # ERROR : 
# # 
# # - TypeError: Images.store_image_df() takes 1 positional argument but 2 were given (line 28)
# # #