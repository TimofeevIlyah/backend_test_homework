class Employee:
    vacation_days = 28
    remaining_vacation_days: int

    def __generate_employee_id(self):
        return hash(self.first_name+self.second_name+self.gender)

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = self.vacation_days
        self._employee_id = self.__generate_employee_id()

    def __str__(self):
        return f'This is a {self.first_name} Employee'

    def consume_vacation(self, days_to_consume):
        if self.remaining_vacation_days >= days_to_consume:
            self.remaining_vacation_days -= days_to_consume

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


class FullTimeEmployee(Employee):
    def __init__(self, first_name, second_name, gender, salary):
        self.__salary = salary
        super().__init__(first_name, second_name, gender)

    def __get_vacation_salary(self):
        return self.__salary*0.8

    def get_unpaid_vacation(self, start_date: str, vacation_days: int):
        return f'Начало неоплачиваемого отпуска: {start_date}, продолжительность: {vacation_days} дней.'


class PartTimeEmployee(Employee):
    vacation_days = 14


full_time_employee = FullTimeEmployee('Robert', 'Cruzoe', 'm', 3000000)
print(full_time_employee.get_unpaid_vacation('2023-07-01', 5))
part_time_employee = PartTimeEmployee('Alena', 'Pyatnitskaya', 'f')
print(part_time_employee.get_vacation_details())
print(full_time_employee._employee_id)
#print(full_time_employee.__get_vacation_salary)