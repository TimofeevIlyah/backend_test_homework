# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os

# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node: Node, idx: int) -> Node:
    current_idx: int = 0
    current_node: Node = node
    prior_node = None
    while True:
        if current_idx == idx:
            if prior_node is None:  # удаляем нулевой элемент
                return current_node.next_item  # начальным стал первый
            else:  # удаляем первый и далее
                if current_node.next_item is None:  # это был последнйи элемент
                    prior_node.next_item = None
                else:  # это был элемент в середине списка
                    prior_node.next_item = current_node.next_item
                return node  # начальный элемент не меняется
        else:
            current_idx += 1
            prior_node = current_node
            current_node = current_node.next_item
        if current_node is None:
            return node


def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м")
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 3)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
