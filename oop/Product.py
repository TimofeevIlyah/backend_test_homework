class Product:
    def __init__(self, name: str, amount: int):
        self.name = name
        self.amount = amount
        pass

    def get_info(self):
        return f'{self.name} (в наличии: {self.amount})'


class Kettlebell(Product):
    def __init__(self, name, amount, weight: float):
        self.weight = weight
        super().__init__(name, amount)

    def get_weight(self):
        return f'{self.get_info()}. Вес: {self.weight} кг'


class Clothing(Product):
    def __init__(self, name, amount, size: str):
        self.size = size
        super().__init__(name, amount)

    def get_size(self):
        return f'{self.get_info()}. Размер: {self.size}'


small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
