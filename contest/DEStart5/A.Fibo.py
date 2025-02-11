def fibo(number: int) -> int:
    if number <= 1:
        return 1
    return fibo(number - 1) + fibo(number - 2)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        version = int(f.readline().strip())
    print(fibo(version))
