"""
Задача 7
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
from os import path, getcwd
from json import dump, dumps


def main():
    src_f_name = path.join(getcwd(), 'task_7_test')
    dst_f_name = path.join(getcwd(), 'task_7_test.json')
    firm_list_average = dict()
    if path.exists(src_f_name):
        with open(src_f_name, 'r') as src:
            for line in src.readlines():
                try:
                    name, property_id, income, expenses = line.split()
                    firm_list_average[name] = int(income) - int(expenses)
                except ValueError as e:
                    print(e)
                    pass
        common = dict()
        common['average'] = sum(firm_list_average.values())
        data = [firm_list_average, common]
        print(dumps(data))
        with open(dst_f_name, 'w+') as dst:
            dump(data, dst)


if __name__ == '__main__':
    main()
