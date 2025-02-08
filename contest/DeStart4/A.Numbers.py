def min_numbers(input: list) -> str:
    result: list = []
    for i in range(len(input)):
        amount: int = 0
        for j in range(len(input)):
            if input[j] < input[i]:
                amount += 1
        result.append(amount)
    return ' '.join(str(x) for x in result)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        nums = list(map(int, f.readline().split()))
    print(min_numbers(nums))
