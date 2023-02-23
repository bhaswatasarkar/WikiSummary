# import wikipedia as wp
# def extract_images(url):
#     query = "Indian history"
#     wp_page = wp.page(query)
#     list_img_urls = wp_page.images
#     print(list_img_urls[0])

from bs4 import BeautifulSoup
import urllib.request
import re
def extract_images(url):
    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page,"html.parser")
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))

    print(images)