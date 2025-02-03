import array


def valid_mountain_array(heights: array.array) -> bool:
    n = len(heights)
    if n < 3:
        return False

    peak_reached = False
    previous = heights[0]

    for i in range(1, n):
        current = heights[i]

        if current > previous:
            if peak_reached:
                # После убывания снова начался рост
                return False
        elif current < previous:
            if not peak_reached:
                # Первое убывание должно быть после хотя бы одного роста
                if i == 1:
                    # Массив начал убывать сразу
                    return False
                peak_reached = True
        else:
            # Плато (равные соседние элементы)
            return False

        previous = current

    # Проверяем, что пик был достигнут
    return peak_reached


def main():
    with open('input.txt', 'r') as f:
        heights = array.array('i', list(map(int, f.readline().split())))
    print(valid_mountain_array(heights))


if __name__ == '__main__':
    main()
