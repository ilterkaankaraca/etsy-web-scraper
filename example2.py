import ews
for i in range(10):
    #ews.checkConnection('https://www.etsy.com/shop/TurkishRugStory')
    print(ews.getSales('https://www.etsy.com/shop/TurkishRugStory'))