from numpy import empty
import requests
from bs4 import BeautifulSoup
import pandas

def get_sale_number(link : str):
  html_text = requests.get(link).text
  soup = BeautifulSoup(html_text, 'html.parser')
  if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
    sale_number = soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}).text[:-6].replace(',','')
  else:
    sale_number = None
  return sale_number


