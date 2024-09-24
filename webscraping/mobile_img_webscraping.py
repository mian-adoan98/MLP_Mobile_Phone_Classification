## Image Data Collection: Webscraping

import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


# send a request to coolblue.com
# orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443"
orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443%2C5463%2C6203%2C5468%2C6196"
orange_response = requests.get(orange_url)

# check if request was successfull
def check_status_request(web_response):
  if web_response.status_code == 200: 
    html_content = web_response.text
    return html_content
  else: 
    failed_status_code = web_response.status_code
    print(f"Failed to retrieve the webpage; status code: {failed_status_code}")

orange_html = check_status_request(orange_response)
# print(orange_html)

# parse html content
orange_soup = BeautifulSoup(orange_html, "html.parser")
all_images = orange_soup.find_all("img")
# print(all_images)

# extract images url
def extract_images(images, url):
  images_url = []
  for img in images:
    src = img.get("src")
    if src:
      # handle relative img urls
      if not src.startswith("http"):
        src = url + src
      images_url.append(src)
  return images_url

images_url_list = extract_images(all_images, orange_url)

# iterate images line by line
for i,image_link in enumerate(images_url_list):
  print(f"Image {i} {image_link}")

# store the image url resources into a pandas dataframe
def store_image_df(image_url_list):
  image_data = pd.DataFrame(image_url_list, columns=["Image_URL"])
  return image_data

image_df = store_image_df(images_url_list)

# save the image data as a csv_file format
image_df.to_csv("image_data.csv")

