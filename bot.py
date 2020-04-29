import telebot
import config

from telebot import types

def CD_parser():
    import requests
    from bs4 import BeautifulSoup as BS

    R_CreditDnipro = requests.get("https://creditdnepr.com.ua/currency")
    html = BS(R_CreditDnipro.content, 'html.parser')
    BigBlock = html.find('div', class_='table-overlay')
    SmallBlock = BigBlock.find('tr', class_='even')
    items = SmallBlock.find_all('td', style='text-align: center')
    buy = items[1]
    sell = items[2]
    print('КредитДніпро')
    print('Купівля = ', buy.get_text())
    print('Продаж = ', sell.get_text())
    CD_buy = buy.get_text()
    CD_sell = sell.get_text()

    CD_message = 'Купівля = ' + CD_buy + ', Продаж = ' + CD_sell
    # R_PUMB = requests.get(" ")
    # R_Privat = requests.get(" ")
    return(CD_message)
CD_message=CD_parser()

bot = telebot.TeleBot(config.TOKEN)

buttons = ('CreditDnipro', 'PrivatBank', 'HBU')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    def Keyboard():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for button in buttons:
            item=types.KeyboardButton(button)
            markup.add(item)
        return(markup())
    Keyboard()
    bot.send_message(message.chat.id, "Тестовий бот перевірки курсу валют".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'CreditDnipro':
            bot.send_message(message.chat.id, str(CD_message))
        elif message.text == 'PrivatBank':
            bot.send_message(message.chat.id, str('PrivatBank no data'))
        elif message.text == 'NBU':
            bot.send_message(message.chat.id, str('NBU no data'))
        else:
            bot.send_message(message.chat.id, message.text)


#RUN
bot.polling(none_stop=True)
