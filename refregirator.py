from datetime import datetime, date, timedelta
from decimal import Decimal

goods = dict()
DATE_FORMAT = '%Y-%m-%d'

def is_date(string):
    value = str(string)
    try:
        result = bool(datetime.strptime(value, DATE_FORMAT))
    except ValueError:
        result = False
    return result

def is_decimal(string):
    value = str(string)
    try:
        result = bool(Decimal(value))
    except ValueError:
        result = False
    return result

def add(items: dict, title: str, amount: Decimal, expiration_date = None):
    if title not in items.keys():
        items[title] = []
    
    if is_date(expiration_date):
        expiration_date = datetime.strptime(str(expiration_date), DATE_FORMAT).date()
        
    items[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})

def add_by_note(items: dict, note: str):
    params = str.split(note)
    has_date = False
    expiration_date = None
    if is_date(params[-1]):
        expiration_date = str(params[-1])
        expiration_date = datetime.strptime(expiration_date, DATE_FORMAT).date()
        has_date = True
     
    #print(-1 - (1 if has_date else 0))
    #print(params[])
    amount_position = -1 - (1 if has_date else 0)
    if is_decimal(params[amount_position]):
        amount = Decimal(params[amount_position])
        
    title = ''
    for param in params[0:amount_position]:
        title += ' ' + param
    title = title.strip()
    add(items, title, amount, expiration_date)


def find(items, needle):
    needle = needle.lower()
    result = []
    for item in items:
        if item.lower().find(needle)>=0:
            result.append(item)
    return result


def amount(items, needle):
    result = Decimal('0')
    founded_needle = find(items, needle)
    for fn in founded_needle:        
        for founded_good in items[fn]:
            result +=founded_good['amount']
    return result


def expire(items, in_advance_days = 0):
    result = []
    in_advance_date = date.today() + timedelta(days = in_advance_days)    
    for item in items:
        expired_amount = Decimal('0')
        for founded_good in items[item]:
            if founded_good['expiration_date'] is not None and founded_good['expiration_date']<=in_advance_date:
                expired_amount += founded_good['amount']
        if expired_amount>0:
            result.append((item, expired_amount))
    return result

    
add(goods, 'Молоко', 10, '2024-12-14')
add(goods, 'Молоко', 2, '2024-12-20')
add(goods, 'Вода', 1.5)
add_by_note(goods, 'Яблоки зеленые 15.3 2024-12-30')
add_by_note(goods, 'Груши моченые 5.6')
add_by_note(goods, 'Сидр 0.5')
add_by_note(goods, 'Сидр 1.5')
add(goods, 'Молочный коктейль', 10)

#print(datetime.strptime('1211', DATE_FORMAT))
#print(find(goods, 'моло'))
#print(amount(goods, 'Моло'))
#print(expire(goods))
print(expire(goods, 10))