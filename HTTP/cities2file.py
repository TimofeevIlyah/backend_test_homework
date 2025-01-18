import requests
import os


cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    try:
        response = requests.get(make_url(city), params=make_parameters())
        response.raise_for_status()
        if response.status_code == 200:
            return response.text
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<ошибка на сервере погоды>'  # ошибка в обучалке. Принимает именно так, а не '<сетевая ошибка>'


for city in cities:
    weather_report = what_weather(city)
    os.makedirs('data', exist_ok=True)
    with open(f'data/{city}.txt', 'w', encoding='utf-8') as weather_file:
        weather_file.write(weather_report+'\n')
