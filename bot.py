import telebot
import config
from parser import CD_message
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Hello.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("КредитДніпро")
    item2 = types.KeyboardButton("Button 2")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Тестовий бот перевірки курсу валют".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

  #  bot.send_message(message.chat.id, "Привіт {0.first_name}.  Вітаю в тестовому боті.".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'КредитДніпро':
            bot.send_message(message.chat.id, str(CD_message))
        elif message.text == 'Button 2':
            bot.send_message(message.chat.id, str('Button 2 working'))
        else:
            bot.send_message(message.chat.id, message.text)


#RUN
bot.polling(none_stop=True)
