def calc(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num

    average = total_sum / len(numbers)
    return total_sum, average


numbers = [10, 20, 30, 40, 50]
total, avg = calc(numbers)
print(f'Сумма: {total}')
print(f'Среднее: {avg}')

numbers = [11, 22, 33, 42, 51]
total, avg = calc(numbers)
print(f'Сумма: {total}')
print(f'Среднее: {avg}')
