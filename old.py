from math import sqrt
from typing import Optional, Union


def add_numbers(number_1: Union[int, float],
                number_2: Union[int, float]) -> Union[int, float]:
    return number_1 + number_2


def calculate_squre_root(number: Union[int, float]) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if your_number <= 0:
        return None
    return 'Мы вычислили квадратный корень из введённого вами числа. Это' \
           f'будет: {calculate_squre_root(your_number)}'
