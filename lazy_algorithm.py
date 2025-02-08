def find_two_indexes(data, expected_sum) -> tuple:
    i1: int = 0
    i2: int = len(data) - 1
    step_begin: bool = True
    while True:
        if i1 == i2 or i1 > i2:
            return ()
        if data[i1]+data[i2] == expected_sum:
            return (i1, i2)
        if step_begin is True:
            i1 += 1
        else:
            i2 -= 1
        step_begin = not step_begin


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_sum = 10
    print(find_two_indexes(data, expected_sum))
