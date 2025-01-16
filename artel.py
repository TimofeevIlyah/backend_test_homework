# Импортируйте необходимые модули.
from datetime import datetime


# Укажите два параметра функции:
def validate_record(name_src: str, birth_date_src: str):
    try:
        datetime.strptime(birth_date_src, '%d.%m.%Y')
    except ValueError:
        print('Некорректный формат даты в записи: '
              f'{name_src}, {birth_date_src}')
        return False
    else:
        return True
    # Напишите код, верните булево значение.


# Укажите параметры функции:
def process_people(data):
    good_count = 0
    bad_count = 0
    for person in data:
        if validate_record(person[0], person[1]):
            good_count += 1
        else:
            bad_count += 1
    return {
        'good': good_count,
        'bad': bad_count
    }
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.


data = [
    ('Иван Иванов', '10.01.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]
statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
print(f'Корректных записей: {statistics['good']}')
print(f'Некорректных записей: {statistics['bad']}')
