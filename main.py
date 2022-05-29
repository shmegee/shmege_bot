from io import BytesIO

import telebot
from telebot import types
import requests
import bs4
import BotGames
from all_menu import Menu, Users
import json
from io import BytesIO
import random
import wikipedia, re
from cars import get_info, get_info1, get_info2, get_info3
from cars import get_image, get_image1, get_image2, get_image3
from cars import get_offer, get_offer1, get_offer2, get_offer3
from weather import get_weather
from config import open_weather_token
from geopy.geocoders import Nominatim
wikipedia.set_lang("ru")
bot = telebot.TeleBot('5372113245:AAEv2nhvtTrVr82HC39ss2c_8al6XisSZIY')

@bot.message_handler(commands="start")
def command(message, res=False):
    chat_id = message.chat.id

    txt_message = f"Привет, {message.from_user.first_name}! Я бот Шмеге!"
    bot.send_message(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)


@bot.message_handler(content_types=['sticker'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    sticker = message.sticker
    bot.send_message(message.chat.id, sticker)

    # глубокая инспекция объекта
    # import inspect,pprint
    # i = inspect.getmembers(sticker)
    # pprint.pprint(i)


@bot.message_handler(content_types=['audio'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    audio = message.audio
    bot.send_message(chat_id, audio)


@bot.message_handler(content_types=['voice'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    voice = message.voice
    bot.send_message(message.chat.id, voice)


@bot.message_handler(content_types=['photo'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    photo = message.photo
    bot.send_message(message.chat.id, photo)


@bot.message_handler(content_types=['video'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    video = message.video
    bot.send_message(message.chat.id, video)


@bot.message_handler(content_types=['document'])
def get_messages(message):
    chat_id = message.chat.id
    mime_type = message.document.mime_type
    bot.send_message(chat_id, "Это " + message.content_type + " (" + mime_type + ")")

    document = message.document
    bot.send_message(message.chat.id, document)
    if message.document.mime_type == "video/mp4":
        bot.send_message(message.chat.id, "This is a GIF!")

@bot.message_handler(content_types=['location'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    location = message.location
    bot.send_message(message.chat.id, location)


@bot.message_handler(content_types=['contact'])
def get_messages(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Это " + message.content_type)

    contact = message.contact
    bot.send_message(message.chat.id, contact)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    chat_id = message.chat.id
    ms_text = message.text

    cur_user = Users.getUser(chat_id)
    if cur_user == None:
        cur_user = Users(chat_id, message.json["from"])

    result = goto_menu(chat_id, ms_text)  # попытаемся использовать текст как команду меню, и войти в него
    if result == True:
        return  # мы вошли в подменю, и дальнейшая обработка не требуется

    cur_menu = Menu.getCurMenu(chat_id)
    if cur_menu != None and ms_text in cur_menu.buttons:  # проверим, что команда относится к текущему меню

        if ms_text == "Помощь":
            send_help(chat_id)

        elif ms_text == "Меню":
            goto_menu(chat_id, "Главное меню")


        elif ms_text== "Выход":
            goto_menu(chat_id, "Меню")


        elif ms_text == "Города":
            city = bot.send_message(chat_id, 'Начнем играть в города')
            bot.register_next_step_handler(city, city_game)

        elif ms_text == "Карту!":
            game21 = BotGames.getGame(chat_id)
            if game21 == None:  # если мы случайно попали в это меню, а объекта с игрой нет
                goto_menu(chat_id, "Выход")
                return

            text_game = game21.get_cards(1)
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

            if game21.status != None:  # выход, если игра закончена
                BotGames.stopGame(chat_id)
                goto_menu(chat_id, "Выход")
                return

        elif ms_text == "Стоп!":
            BotGames.stopGame(chat_id)
            goto_menu(chat_id, "Выход")
            return


        elif ms_text == "2107":
            bot.send_photo(chat_id, get_image())
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url='https://auto.ru/sankt-peterburg/cars/vaz/2107/all/')
            markup.add(btn1)
            bot.send_message(chat_id, text=get_info(), reply_markup=markup)

        elif ms_text == "2114":
            bot.send_photo(chat_id, get_image1())
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url='https://auto.ru/sankt-peterburg/cars/vaz/2114/all/')
            markup.add(btn1)
            bot.send_message(chat_id, text=get_info1(), reply_markup=markup)

        elif ms_text == "НИВА":
            bot.send_photo(chat_id, get_image2())
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url='https://auto.ru/sankt-peterburg/cars/vaz/2121/all/')
            markup.add(btn1)
            bot.send_message(chat_id, text=get_info2(), reply_markup=markup)

        elif ms_text == "Vesta":
            bot.send_photo(chat_id, get_image3())
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Перейти на сайт", url='https://auto.ru/sankt-peterburg/cars/vaz/vesta/all/')
            markup.add(btn1)
            bot.send_message(chat_id, text=get_info3(), reply_markup=markup)

        elif ms_text == "Моя погода":
            #bot.send_chat_action(message.from_user.id, 'find_location')
            bot.send_message(chat_id, text=get_weather('petersburg', open_weather_token))
            #bot.send_message(chat_id, text=message.location)
           #bot.send_message(chat_id, text=get_weather('petersburg', open_weather_token))


        elif ms_text == "Москва":
            bot.send_message(chat_id, text=get_weather('moscow', open_weather_token))

        elif ms_text == "Минск":
            #bot.send_chat_action(message.from_user.id, 'find_location')
            bot.send_message(chat_id, text=get_weather('minsk', open_weather_token))
            #bot.send_message(chat_id, text=message.location)



    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Мне жаль, я не понимаю вашу команду: " + ms_text)
        goto_menu(chat_id, "Главное меню")

# -----------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # если требуется передать параметр или несколько параметров в обработчик кнопки, использовать методы Menu.getExtPar() и Menu.setExtPar()
    pass
    # if call.data == "ManOrNot_GoToSite": #call.data это callback_data, которую мы указали при объявлении InLine-кнопки
    #
    #     # После обработки каждого запроса нужно вызвать метод answer_callback_query, чтобы Telegram понял, что запрос обработан.
    #     bot.answer_callback_query(call.id)

# -----------------------------------------------------------------------
def goto_menu(chat_id, name_menu):
    # получение нужного элемента меню
    cur_menu = Menu.getCurMenu(chat_id)
    if name_menu == "Выход" and cur_menu != None and cur_menu.parent != None:
        target_menu = Menu.getMenu(chat_id, cur_menu.parent.name)
    else:
        target_menu = Menu.getMenu(chat_id, name_menu)

    if target_menu != None:
        bot.send_message(chat_id, text=target_menu.name, reply_markup=target_menu.markup)

        # Проверим, нет ли обработчика для самого меню. Если есть - выполним нужные команды
        if target_menu.name == "Игра в 21":
            game21 = BotGames.newGame(chat_id, BotGames.Game21(jokers_enabled=True))  # создаём новый экземпляр игры
            text_game = game21.get_cards(2)  # просим 2 карты в начале игры
            bot.send_media_group(chat_id, media=getMediaCards(game21))  # получим и отправим изображения карт
            bot.send_message(chat_id, text=text_game)

        elif target_menu.name == "Камень, ножницы, бумага":
            gameRSP = BotGames.newGame(chat_id, BotGames.GameRPS())  # создаём новый экземпляр игры
            text_game = "<b>Победитель определяется по следующим правилам:</b>\n" \
                        "1. Камень побеждает ножницы\n" \
                        "2. Бумага побеждает камень\n" \
                        "3. Ножницы побеждают бумагу"
            bot.send_photo(chat_id, photo="https://i.ytimg.com/vi/Gvks8_WLiw0/maxresdefault.jpg", caption=text_game, parse_mode='HTML')

        return True
    else:
        return False


# -----------------------------------------------------------------------
def getMediaCards(game21):
    medias = []
    for url in game21.arr_cards_URL:
        medias.append(types.InputMediaPhoto(url))
    return medias


# -----------------------------------------------------------------------
def send_help(chat_id):
    global bot
    bot.send_message(chat_id, "shmege")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://vk.com/shmege")
    markup.add(btn1)
    img = open('shmege.jpg', 'rb')
    bot.send_photo(chat_id, img, reply_markup=markup)

    bot.send_message(chat_id, "Активные пользователи чат-бота:")
    for el in Users.activeUsers:
        bot.send_message(chat_id, Users.activeUsers[el])








 

bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()