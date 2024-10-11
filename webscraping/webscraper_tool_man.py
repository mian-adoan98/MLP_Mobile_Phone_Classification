## Webscraping Tool maangement

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


# send a request to coolblue.com
# orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443"
orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443%2C5463%2C6203%2C5468%2C6196"
orange_response = requests.get(orange_url)

# Webscraper lass 
class Webscraper:
  def __init__(self, response): 
    self.response = response

  # check if request was successfull
  def check_status_request(self):
    if self.response.status_code == 200: 
      html_content = self.response.text
      print(f"Response Satus Code: {self.response.status_code}")
      return html_content
    else: 
      failed_status_code = self.response.status_code
      print(f"Failed to retrieve the webpage; status code: {failed_status_code}")
  
  def create_parser(self, html_content):
    # parse html content
    web_soup = BeautifulSoup(html_content, "html.parser")
    return web_soup

# Image Scraper class
class Images: 
  def __init__(self, images):
    self.images = images 
  # extract images url
  def extract_images(self,url):
    images_url = []
    for img in self.images:
      src = img.get("src")
      if src:
        # handle relative img urls
        if not src.startswith("http"):
          src = url + src
        images_url.append(src)
    return images_url
  
    # store the image url resources into a pandas dataframe
  def store_image_df(image_url_list):
    image_data = pd.DataFrame(image_url_list, columns=["Image_URL"])
    return image_data

# Label Scraper class
class Labels:
  def __init__(self, labels):
    self.labels = labels

  def extract_labels(self):
    pass

  def store_labels(self):
    pass 
  
# iterate images line by line
def iterate_images(images_url_list):
  for i,image_link in enumerate(images_url_list):
    print(f"Image {i} {image_link}")

