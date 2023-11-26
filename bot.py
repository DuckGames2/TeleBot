import telebot
from telebot import types

token = '6906596511:AAGcBEIpH26rG5CYtdxGJp0Bn4eW8UizKws'
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start_message(message):
    mess = f'Привет,{message.from_user.first_name}'
    bot.send_message(message.chat.id,mess, parse_mode = 'html')

@bot.message_handler(commands=['Website'])
def info(message):
    n1 = types.InlineKeyboardMarkup()
    n2 = types.InlineKeyboardButton('website', url='https://gdz.ru/class-9/russkii_yazik/')
    n1.add(n2)
    n3 = types.InlineKeyboardMarkup()
    n4 = types.InlineKeyboardButton('website', url='https://gdz.ru/class-9/geometria/')
    n3.add(n4)
    bot.send_message(message.chat.id, 'Посетите 1сайт', reply_markup=n1)
    bot.send_message(message.chat.id, 'Посетите 2сайт', reply_markup=n3)

@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_message(message.chat.id,'Ух ты какой прикольный стикер', parse_mode='html')



bot.polling(none_stop=True)

