from numpy import empty
import requests
from bs4 import BeautifulSoup
import pandas

excel = pandas.read_excel("2.xlsx")
links=excel[excel.columns[0]]
names=excel[excel.columns[1]]
vgm_url = ''
sales={}
for i in range(len(links)):
    if pandas.notna(links[i]):
        print(str(i) + '--' + str(links[i]))
        vgm_url = str(links[i])
        html_text = requests.get(vgm_url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        if soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}) is not None:
            sales[links[i]] = soup.body.find('span', attrs={'class': 'wt-text-caption wt-no-wrap'}).text

        else:
            sales[links[i]] = '-'
    else:
        sales['empty'+str(i)] = 'empty'+str(i)
df = pandas.DataFrame(data=sales, index=[0])
print(names)
df=df.T
df['Name'] = names.to_list()
df.to_excel('sales.xlsx')

