from telebot import types

class KeyboardButton:
    def __init__(self, name, handler=None):
        self.name=name
        self.handler=handler

class Users:
    activeUsers = {}

    def __init__(self, chat_id, user_json):
        self.id = user_json["id"]
        self.isBot = user_json["is_bot"]
        self.firstName = user_json["first_name"]
        self.userName = user_json["username"]
        self.languageCode = user_json["language_code"]

        self.__class__.activeUsers[chat_id] = self

    def __str__(self):
        return f"Name user: {self.firstName}   id: {self.userName}   lang: {self.languageCode}"

    @classmethod
    def getUser(cls, chat_id):
        return cls.activeUsers.get(chat_id)

class Menu:
    hash = {}
    cur_menu = {}
    extendedParameters = {}
    def __init__(self, name, buttons=None, parent=None, handler=None):
        self.parent = parent
        self.name = name
        self.buttons = buttons
        self.handler = handler

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        markup.add(*buttons)
        self.markup = markup

        self.__class__.hash[name] = self

    @classmethod
    def getExtPar(cls, id):
        return cls.extendedParameters.pop(id, None)

    @classmethod
    def setExtPar(cls, parameter):
        import uuid
        id = uuid.uuid4().hex
        cls.extendedParameters[id] = parameter
        return id

    @classmethod
    def getMenu(cls, chat_id, name):
        menu = cls.hash.get(name)
        if menu != None:
            cls.cur_menu[chat_id] = menu
        return menu

    @classmethod
    def getCurMenu(cls, chat_id):
        return cls.cur_menu.get(chat_id)

main_menu = Menu("Главное меню", buttons=["Погода", "Наш автопром!", "Игра в 21"])
ochko = Menu("Игра в 21", buttons = ["Карту!", "Стоп!", "Меню"])
weather_menu = Menu("Погода", buttons=["Моя погода","Москва", "Минск" ,"Меню"])
cars_menu = Menu("Наш автопром!", buttons=["ВАЗ", "Меню"])
vaz_menu = Menu("ВАЗ", buttons =["2107", "2114", "НИВА", "Vesta", "Меню"])