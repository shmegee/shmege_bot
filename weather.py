import requests
from config import open_weather_token
from pprint import pprint
from geopy.geocoders import Nominatim





def get_weather(city, token):
    global bot
    code_emoji = {
        "Clear": "Оставь зонт дома",
        "Clouds": "Возможны осадки",
        "Rain": "Не забудь зонт!",
        "Drizzle": "Не забудь зонт и теплую одежду!",
        "Thunderstorm": "Гроза, не стой под деревьями!",
        "Snow": "Let it snow, let it snow....",
        "Mist": "Включай противотуманки!"
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        city = data["name"]
        q = round(data["main"]["temp"])
        weather_description = data["weather"][0]["main"]
        if weather_description in code_emoji:
            wd = code_emoji[weather_description]
        else:
            wd = "Спроси у бабушки, как одеться)"

        hum = data["main"]["humidity"]
        press = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        return (f"В городе {city}:\nТемпература: {q} {wd}\nДавление: {press}мм.рт.ст.\nВлажность: {hum}%\nСкорость ветра: {wind}м/с\n\n"
              f"Хорошего дня!"
              )
    except Exception as ex:
        return (ex)
        return ("Проверь, верно ли ты написал город")

def get_weather1(lat, long, token):
    global bot
    code_emoji = {
        "Clear": "Оставь зонт дома",
        "Clouds": "Возможны осадки",
        "Rain": "Не забудь зонт!",
        "Drizzle": "Не забудь зонт и теплую одежду!",
        "Thunderstorm": "Гроза, не стой под деревьями!",
        "Snow": "Let it snow, let it snow....",
        "Mist": "Включай противотуманки!"
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=lat={lat}lon={long}&exclude=hourly&appid={open_weather_token}&units=metric")
        data = r.json()
        city = data["name"]
        q = round(data["main"]["temp"])
        weather_description = data["weather"][0]["main"]
        if weather_description in code_emoji:
            wd = code_emoji[weather_description]
        else:
            wd = "Спроси у бабушки, как одеться)"

        hum = data["main"]["humidity"]
        press = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        return (f"В городе {city}:\nТемпература: {q} {wd}\nДавление: {press}мм.рт.ст.\nВлажность: {hum}%\nСкорость ветра: {wind}м/с\n\n"
              f"Хорошего дня!"
              )
    except Exception as ex:
        return (ex)
        return ("Проверь, верно ли ты написал город")
def main():
    city = input("Напиши на английском языке город, в котором хочешь узнать прогноз.\n")
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()



