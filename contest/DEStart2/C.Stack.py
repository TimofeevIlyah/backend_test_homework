class Stack:
    def __init__(self):
        # Для хранения элементов в списке используем приватный атрибут.
        # На его приватность указывают два подчёркивания в имени.
        self.__items = []

    def push(self, item):
        """Добавить элемент в стек."""
        self.__items.append(item)

    def pop(self):
        """Взять элемент из стека."""
        return self.__items.pop()

    def peek(self):
        """Посмотреть последний элемент без изъятия."""
        return self.__items[-1]

    def size(self):
        """Вернуть размер стека."""
        return len(self.__items)


def is_correct_bracket_seq(sequence: str) -> bool:
    stack = Stack()
    opening_bracket = '[({'
    closing_bracket = '])}'
    for i in range(len(sequence)):
        cur_symbol = sequence[i:i+1]
        is_opening = True if opening_bracket.find(cur_symbol) > -1 else False
        is_closing = True if closing_bracket.find(cur_symbol) > -1 else False
        if is_opening:  # если открывается, то пушим в стек
            stack.push(cur_symbol)
        if is_closing:  # если закрывается,
            if stack.size() == 0:  # то провереим пустой ли список
                return False
            else:  # последний из стека и проверяем, соответствие открытия закрытию
                prior_symbol = stack.pop()
                if opening_bracket.find(prior_symbol) != closing_bracket.find(cur_symbol):
                    return False

    return stack.size() == 0


def main():
    with open('input.txt', 'r') as f:
        seq = f.readline()
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':
    main()
