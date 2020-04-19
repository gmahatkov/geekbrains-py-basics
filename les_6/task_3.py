"""
Задача 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income
(доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать
методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу
примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать
методы экземпляров).
"""


class Worker:
    __wage = 0
    __bonus = 0

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    @property
    def _income(self):
        return {
            'wage': self.__wage,
            'bonus': self.__bonus,
        }

    @_income.setter
    def _income(self, value):
        self.__wage = float(value * 0.2)
        self.__bonus = float(value * 0.8)


class Position(Worker):
    def __init__(self, salary, name, surname, position):
        super().__init__(name, surname, position)
        self._income = salary

    @property
    def full_name(self):
        return f'{self.name.title()} {self.surname.title()} at position: {self.position}'

    @property
    def total_income(self):
        try:
            return self._income['wage'] + self._income['bonus']
        except KeyError:
            return 0


if __name__ == '__main__':
    milk_maid = Position(100, 'Ivan', 'Ivanov', 'Milk Maid')
    print('Name: ', milk_maid.full_name)
    print('Total income: ', milk_maid.total_income)

