class Phone:
    dial_type: str

    def __init__(self, dial_type_value=''):
        self.dial_type = dial_type_value if dial_type_value != '' else 'Проводной'

    def ring(self):
        print('Бзз')


my_phone = Phone()
print(my_phone.dial_type)
my_phone.dial_type = 'Кнопочный'
print(my_phone.dial_type)
my_phone.ring()
