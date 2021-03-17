from numpy import empty
import requests
from bs4 import BeautifulSoup
import pandas
from datetime import date

excel = pandas.read_excel("2.xlsx")
links=excel[excel.columns[0]]
names=excel[excel.columns[1]]
vgm_url = ''
sales=[]
for i in range(len(links)):
    if pandas.notna(links[i]):
        print(str(i) + '--' + str(links[i]))
        vgm_url = str(links[i])
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
            sales.append(soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'})).text[:-6].replace(',','')   

        else:
            sales.append( '-')
    else:
        sales.append('empty'+str(i))
df = pandas.DataFrame(data=sales).T
excel[date.today()] = sales
excel.to_excel('2.xlsx')
