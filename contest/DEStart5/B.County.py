def county(numbers: list[int], clock: int, beginner: int = 1) -> list[int]:
    if len(numbers) == 1:
        return numbers

    current_number = numbers.index(beginner)
    current_clock = clock
    while True:
        if current_clock == 1:
            next_number = current_number + 1
            if next_number == len(numbers):
                next_number = 0
            beginner = numbers[next_number]
            numbers.pop(current_number)
            break

        current_number += 1
        if current_number == len(numbers):
            current_number = 0
        current_clock -= 1

    return county(numbers, clock, beginner)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        N = int(f.readline().strip())
        K = int(f.readline().strip())
        numbers = [n + 1 for n in range(N)]
    # print(numbers)
    print(county(numbers, K)[0])
