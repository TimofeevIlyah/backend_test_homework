def list_superset(list_set_1, list_set_2):
    # Не меняйте названия функции и параметров. Напишите решение здесь.
    b1 = all(_ in list_set_1 for _ in list_set_2)
    b2 = all(_ in list_set_2 for _ in list_set_1)
    if b1:
        if b2:
            return 'Наборы равны.'
        else:
            return f'Набор {list_set_1} - супермножество.'
    if b2 and not b1:
        return f'Набор {list_set_2} - супермножество.'
    return 'Супермножество не обнаружено.'


# Примеры для проверки функции.
list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

# list_superset(list_set_1, list_set_2)
print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
