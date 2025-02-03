example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    # Напишите здесь код сортировки.
    last_index = len(data) - 1
    while True:
        # i = 0
        swapped = False
        for i in range(last_index):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
        last_index -= 1
        if not swapped or last_index == 1:
            break
    return data


print(bubble_sort(example_array))
