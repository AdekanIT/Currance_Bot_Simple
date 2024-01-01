from telebot import types


kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
pb = types.ReplyKeyboardMarkup(resize_keyboard=True)
currency = types.KeyboardButton('Currency')
rub = types.KeyboardButton('RUB')
eur = types.KeyboardButton('EUR')
usd = types.KeyboardButton('USD')

kb.add(currency)
pb.add(rub, eur, usd)
