## Image Data Collection: Webscraping

import os
import requests
from bs4 import BeautifulSoup

# send a request to coolblue.com
orange_url = "https://www.orange.lu/en/smartphones/?device_brand=5443"
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
      images_url.append()
  return images_url

images_url_list = extract_images(all_images, orange_url)
print(images_url_list)
