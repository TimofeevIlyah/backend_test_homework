from typing import Optional, Union


def add(x: Union[int, float], z: Union[int, float]) -> Union[int, float]:
    return x + y


def print_name(name: Optional[str]) -> Optional[str]:
    return 'Hello, ' + name if name is not None else 'None'


x: int = 10
y: int = 5
print('сумма: ', add(x, y))

res: Optional[str] = print_name(None)
print(res)

res2: Optional[str] = print_name('Тим')
print(res2)
