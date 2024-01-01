import telebot
from telebot.types import ReplyKeyboardRemove
from button import kb, pb

bot = telebot.TeleBot('6321629280:AAEWVU-hnu9oADtfqWwMPVWprFQEVr_CB5I')


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Hello! Welcome to currency bot!', reply_markup=kb)

@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    if message.text.title() == 'Currency':
        bot.send_message(user_id, 'Enter the currency: ', reply_markup=pb)
        bot.register_next_step_handler(message, currency)
    else:
        bot.send_message(user_id, 'WTF?!')


def  currency(message):
    user_id = message.from_user.id
    if message.text.upper() == 'RUB':
        bot.send_message(user_id, '1 RUB is 138,64 SOM in 01.01.2024', reply_markup=ReplyKeyboardRemove())
    elif message.text.upper() == 'EUR':
        bot.send_message(user_id, '1 EUR is 13 673,18 SOM in 01.01.2024', reply_markup=ReplyKeyboardRemove())
    elif message.text.upper() == 'USD':
        bot.send_message(user_id, '1 USD is 12 373,36 SOM in 01.01.2024', reply_markup=ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'WTF?!')


bot.polling(none_stop=True)