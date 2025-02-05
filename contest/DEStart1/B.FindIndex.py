def find_index(values: list[int], value: int) -> int:
    vl = len(values)
    for i in range(vl):
        if values[i] >= value:
            return i
    return vl


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.readlines()
    raw_array = list(map(int, data[0].split()))
    value = int(data[1])
    print(find_index(raw_array, value))
