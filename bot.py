import telebot
import config
from parser import CD_message
from telebot import types

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
