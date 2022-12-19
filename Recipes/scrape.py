"""
script to refamiliarze with webscraping
"""

from bs4 import BeautifulSoup
import requests

url = ''

page = requests.get(url)
page.content

soup = BeautifulSoup(page.content, 'html.parser')

