def sort_block(array: list[int]) -> int:
    l: int = len(array)

    expected_block_sum, current_block_sum, result = 0, 0, 0
    for i in range(0, l):
        current_block_sum += array[i]
        expected_block_sum += i
        if current_block_sum == expected_block_sum:
            result += 1

    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        block_amount = int(f.readline().strip())
        blocks = list(map(int, f.readline().split()))
    print(sort_block(blocks))
