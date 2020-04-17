import requests
from bs4 import BeautifulSoup as BS 

R_CreditDnipro = requests.get(" https://creditdnepr.com.ua/currency ")
html = BS(R_CreditDnipro.content, 'html.parser')
BigBlock = html.find('div', class_='table-overlay')
SmallBlock = BigBlock.find('tr', class_='even')
items = SmallBlock.find_all('td', style='text-align: center')
buy=items[1]
sell=items[2]
print('КредитДніпро')
print('Купівля = ', buy.get_text())
print('Продаж = ', sell.get_text())
CD_buy = buy.get_text()
CD_sell = sell.get_text()

CD_message = 'Купівля = ' + CD_buy + ', Продаж = ' + CD_sell
#R_PUMB = requests.get(" ")
#R_Privat = requests.get(" ")