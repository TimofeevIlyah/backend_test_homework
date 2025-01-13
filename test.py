class ExInt(int):
    def __str__(self):
        return f'ex{self.__str__}'


ex_int = ExInt()
print(ex_int)
ex_int = 5
print(ex_int)