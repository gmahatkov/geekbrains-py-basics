"""
Задача 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
from os import path, getcwd


def main():
    f_name = path.join(getcwd(), 'task_3_test')
    if path.exists(f_name):
        stuff = dict()
        with open(f_name) as f:
            try:
                for line in f.readlines():
                    name, salary = line.split()[:2]
                    stuff[name] = float(salary)
            except ValueError as e:
                print(e)
                stuff[name] = 0
        for name, salary in stuff.items():
            if salary > 20:
                print(f'Name: {name}; Salary: {salary}')
        mean = sum(stuff.values()) / len(stuff)
        print(f'Mean salary is {mean}')


if __name__ == '__main__':
    main()
