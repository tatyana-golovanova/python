class Worker:
    _income = {
        'wage': 0,
        'bonus': 0,
    }

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.position = None


class Position(Worker):
    _income = {
        'wage': 7000,
        'bonus': 1500,
    }

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Иван', 'Иванов')
print(position.get_full_name())
print(position.get_total_income())
