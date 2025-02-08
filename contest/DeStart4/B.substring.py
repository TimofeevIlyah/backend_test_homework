def find_max_uni(ins: str) -> int:
    max_uni = 0
    sub = ''
    ls = 0
    for i in range(len(ins)):
        c = ins[i]
        found = sub.find(c)
        if found > -1:
            max_uni = max(max_uni, ls)
            sub = sub[found + 1:ls]
        sub += c
        ls = len(sub)
    return max(max_uni, ls)


def find_max_uni_2(s: str) -> int:
    # от DeepSeek
    char_index = {}
    left = 0
    max_length = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
    return max_length


def find_max_uni_3(ins: str) -> int:
    # от Журавлевой
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(ins)):
        while ins[right] in char_set:
            char_set.remove(ins[left])
            left += 1
        char_set.add(ins[right])
        max_length = max(max_length, right - left + 1)
    return max_length


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        symbols = f.readline().strip()
    print(find_max_uni(symbols))
