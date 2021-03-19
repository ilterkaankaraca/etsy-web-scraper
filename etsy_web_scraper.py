from numpy import empty
import requests
from bs4 import BeautifulSoup
import pandas

def getSaleNumber(link : str):
  htmlText = requests.get(link).text
  soup = BeautifulSoup(html_text, 'html.parser')
  if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
    saleNumber = soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}).text[:-6].replace(',','')
  else:
    saleNumber = None
  return saleNumber


