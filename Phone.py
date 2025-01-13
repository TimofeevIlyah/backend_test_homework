class Phone:
    line_type = 'Проводной'

    def __init__(self, dial_type_value=''):
        self.dial_type = dial_type_value
        self._serial_number = id(dial_type_value)

    def ring(self):
        print('Бзз')

    def call(self, phone_number):
        print(f'Звоню по {phone_number}. Тип связи - {self.line_type}')


class MobilePhone(Phone):
    line_type = 'Беспроводной'
    battery_typ = 'Li-ion'

    def __init__(self, dial_type_value='', network_type_value=''):
        self.__network_type = network_type_value
        super().__init__(dial_type_value)

    def ring(self):
        print('Курлык')

    def start_game(self):
        print('Игра запущена')

    def __str__(self):
        return f'Тип набора {self.dial_type}'

    def get_info(self):
        print(
            f'Серийный номер: {self._serial_number},'
            f'тип сети: {self.__network_type}'
        )


my_phone = Phone('Кнопочный')
print(my_phone.dial_type)
my_phone.ring()

mob_phone = MobilePhone('android', 'LTE')
mob_phone.ring()
print(mob_phone)
print(mob_phone._serial_number)
mob_phone.get_info()
