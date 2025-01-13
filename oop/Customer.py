class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, price: float):
        return round(price * (100 - self.__discount) / 100, 2)

    def set_discount(self, discount: float):
        self.__discount = 80 if discount >= 80 else discount


customer = Customer("Иван Иванович")
print(customer.get_price(100))
customer.set_discount(20.1985)
print(customer.get_price(100))
