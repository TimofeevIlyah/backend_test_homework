def delete_duplicates(array: list):
    result = []
    prior = ''
    for item in array:
        if prior == item:
            continue
        else:
            result.append(item)
            prior = item

    result.extend(['_']*(len(array) - len(result)))
    return ' '.join(result)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()
    count = int(data[0])
    raw_array = data[1].split()

    # print(raw_array)
    result = delete_duplicates(raw_array)
    print(result)
