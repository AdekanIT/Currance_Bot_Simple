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
        bot.send_message(user_id, 'How many RUB you wanna take?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, math_rub)
    elif message.text.upper() == 'EUR':
        bot.send_message(user_id, '1 EUR is 13 673,18 SOM in 01.01.2024', reply_markup=ReplyKeyboardRemove())
        bot.send_message(user_id, 'How many EUR you wanna take?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, math_eur)
    elif message.text.upper() == 'USD':
        bot.send_message(user_id, '1 USD is 12 373,36 SOM in 01.01.2024', reply_markup=ReplyKeyboardRemove())
        bot.send_message(user_id, 'How many USD you wanna take?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, math_usd)
    else:
        bot.send_message(user_id, 'WTF?!')


def math_rub(message):
    user_id = message.from_user.id
    num = float(message.text)
    som = num * 138.64
    som = round(som, 2)
    bot.send_message(user_id, f'{som} SOM cost of {num} RUB!', reply_markup=ReplyKeyboardRemove())


def math_eur(message):
    user_id = message.from_user.id
    num = float(message.text)
    som = num * 13673.18
    som = round(som, 2)
    bot.send_message(user_id, f'{som} SOM cost of {num} EUR!', reply_markup=ReplyKeyboardRemove())


def math_usd(message):
    user_id = message.from_user.id
    num = float(message.text)
    som = num * 12373.36
    som = round(som, 2)
    bot.send_message(user_id, f'{som} SOM cost of {num} USD!', reply_markup=ReplyKeyboardRemove())


bot.polling(none_stop=True)