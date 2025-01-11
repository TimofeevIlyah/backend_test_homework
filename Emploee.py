class Employee:
    vacation_days = 28
    remaining_vacation_days: int

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days

    def __str__(self):
        return f'This is a {self.first_name} Employee'

    def consume_vacation(self, days_to_consume):
        if self.remaining_vacation_days >= days_to_consume:
            self.remaining_vacation_days -= days_to_consume

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee = Employee('Robert', 'Cruzoe', 'm')
employee.consume_vacation(7)
print(employee.get_vacation_details())
print(employee)
