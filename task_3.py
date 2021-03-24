salary_dict = {'wage': 1000, 'bonus': 200}

class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'driller'
    _income = salary_dict

class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname
    def get_full_income(self):
        return sum(self._income.values())


a = Position()
print(a.get_full_name())
print(a.get_full_income())