import telebot
from telebot import types
import random
token = '6949946381:AAFyKyWq_2yWsVdeGLJLY2HXYfKyCIArfaM'
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start_message(message):
    mess = f'Привет,<b>{message.from_user.first_name}</b> <U>{message.from_user.last_name}</U>'
    bot.send_message(message.chat.id,mess, parse_mode = 'html')

@bot.message_handler(commands=['help'])  # выполнение команды "help"
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)  # создание объекта кнопки. ReplyKeyboardMarkup(resize_keyboard= Trueменяет под устройство) - кнопки внизу панели
    start = types.KeyboardButton('/start')  # InlineKeyboardMarkup - кнопки в текстовом сообщении
    inf = types.KeyboardButton ('Данные о пользователе')  # название кнопки
    markup.add(start, inf)  # Создание кнопки, по нажатию которой отправит '/start'
    bot.send_message(message.chat.id, 'Команды для бота', reply_markup=markup)
@bot.message_handler(commands=['Website'])
def info(message):
    n1 = types.InlineKeyboardMarkup()
    n2 = types.InlineKeyboardButton('website', url='https://gdz.ru/')
    n1.add(n2)
    bot.send_message(message.chat.id, 'Посетите сайт', reply_markup=n1)

# Список идентификаторов стикеров
sticker_ids = [
    'CAACAgIAAxkBAAEB7uJlUOk1aRmQCgLgvcMLVmXUvIJnlAACoAADlp-MDmce7YYzVgABVTME',
    'CAACAgIAAxkBAAEB7uRlUOlWriErrHBhLOu1sUlKwqdR1QACwi4AAuJUIUtpSs4e3PowOTME',
    'CAACAgIAAxkBAAEB7uZlUOmA7_4w3E2TNye1uRkg-axSyAACuw0AAuYAASFL9-t-HOXBDy8zBA',
    'CAACAgIAAxkBAAECCrVlWdF6KmsV3GqojOcx9xQNW7qRcAAC5zAAAjDteUgES_ShXX4KKTME',
    'CAACAgIAAxkBAAECCrNlWdFVbfbLOqQyLCDgo87pwPW5BgAC4x8AAoM40EtDdfhMIzfvITME'
    # Добавьте еще идентификаторы стикеров по вашему выбору
]


@bot.message_handler(content_types='sticker')
def handle_sticker(message):
        random_sticker_id = random.choice(sticker_ids)
        bot.send_sticker(message.chat.id, random_sticker_id)



userchoice = {}
game_options = ['Камень','Ножницы','Бумага']

@bot.message_handler(commands=['game'])
def start_game(message):
    bot.send_message(message.chat.id,'Давай сыграем в игру, выбери камень, ножницы или бумагу')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    Stone = telebot.types.KeyboardButton('Камень')
    Paper = telebot.types.KeyboardButton('Бумага')
    Snip = telebot.types.KeyboardButton('Ножницы')
    keyboard.add(stone, paper, snip)

    bot.send_message(message.chat.id, 'Выберите вариант ответа',reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handler(message):
    user_choice = message.text
    bot_chice = random.choice(game_options)
    if user_choice in game_options:
        win = winner(user_choice,bot_choice)

        result_message = f'Пользователь выюрал {user_choice},Бот выбрал{bot_choice}.\n'
        result_message = f'{win}'
        bot.send_message(message.chat.id, result_message)





def winner(user_choice,bot_choice):
    if user_choice == bot_choice:
        return 'Ничья'
    elif (
        (user_choice == 'Камень' and bot_choice == 'Ножницы')or
         (user_choice == 'Ножницы' and bot_choice == 'Бумага')or
         (user_choice == 'Бумага' and bot_choice == 'Камень')
         ):
        return 'Ты победил'
    else:
        return 'Бот победил'


@bot.message_handler(commands=['dog'])
def handle_start(message):
    user_id = message.from_user.id
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки для выбора животных
    cat_button = types.InlineKeyboardButton("Кот", callback_data="cat")
    dog_button = types.InlineKeyboardButton("Собака", callback_data="dog")
    lion_button = types.InlineKeyboardButton("Лев", callback_data="lion")

    # Добавляем кнопки в разметку
    markup.add(cat_button, dog_button, lion_button)

    # Отправляем сообщение с кнопками
    bot.send_message(user_id, "Выбери животное:", reply_markup=markup)


# Обработчик обратных вызовов
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    animal = call.data

    # Ответы для каждого животного
    responses = {
        "cat": "Коты мягкие и пушистые животные.",
        "dog": "Собаки верные друзья человека.",
        "lion": "Львы - короли джунглей."
    }

    response = responses.get(animal, "Я не знаю такого животного.")

    # Отправляем ответ пользователю
    bot.send_message(user_id, response)




# Запускаем бота
bot.polling()

@bot.message_handler(content_types = ['text'])
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'{message.from_user.id}', parse_mode='html')
    elif message.text == 'Загадка':
        bot.send_message(message.chat.id, '<U><b>Висит груша нельзя скушать!?</b></U>', parse_mode='html')
    elif message.text == 'Фото':
        photo = open('phytone photo.jfif','rb')
        bot.send_photo(message.chat.id,photo)
    elif message.text == 'Отправь документ':
        doc = open('DOC1.docx','rb')
        bot.send_document(message.chat.id,document = doc, caption = 'Важнейший файл')
    elif message.text == 'Данные о пользователе':
        bot.send_message(message.chat.id,f'{message.from_user}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'я тебя не понимаю', parse_mode='html')
@bot.message_handler(content_types=['document'])
def get_user_doc(message):
    bot.send_message(message.chat.id,'Документ принят', parse_mode='html')



@bot.message_handler(commands=['help'])  # выполнение команды "help"
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard= True,row_width=1)  #создание объекта кнопки. ReplyKeyboardMarkup(resize_keyboard= Trueменяет под устройство) - кнопки внизу панели
    start = types.KeyboardButton('/start')#  InlineKeyboardMarkup - кнопки в текстовом сообщении
    inf = types.KeyboardButton('Данные о пользователе')#название кнопки
    markup.add(start, inf)                     # Создание кнопки, по нажатию которой отправит '/start'
    bot.send_message(message.chat.id, 'Команды для бота', reply_markup=markup)









@bot.message_handler(content_types=['text'])
def get_user_photo(message):
    photo = 'phytone photo.jfif'
    bot.send_photo(message.chat.id,photo=photo, caption='Логотип  Питона')
    bot.send_message(message.chat.id,'крутое фото',parse_mode = 'html')


bot.polling(none_stop=True)
