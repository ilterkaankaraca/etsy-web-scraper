from numpy import empty
import requests
from bs4 import BeautifulSoup
import pandas

def get_sales(link : str):
  request = requests.get(link)
  html_text = request.text
  status = request.status_code
  soup = BeautifulSoup(html_text, 'html.parser')
  if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
    sale_number = soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}).text[:-6].replace(',','')
  elif soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is None or status[0]!='2':
    sale_number = '-'
  return sale_number