import pandas
import ews
excel = pandas.read_excel("2.xlsx")
links=excel[excel.columns[0]]
names=excel[excel.columns[1]]
vgm_url = ''
sales={}
for i in range(len(links)):
    if pandas.notna(links[i]):
        print(str(i) + '--' + str(links[i]))
        sales[links[i]]= ews.get_sales(links[i])
    else:
        sales['empty'+str(i)] = 'empty'+str(i)
df = pandas.DataFrame(data=sales, index=[0])
df=df.T
df['Name'] = names.to_list()
df.to_excel('sales.xlsx')

