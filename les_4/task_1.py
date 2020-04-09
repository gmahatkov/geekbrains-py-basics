"""
Задача 1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""


def calc_salary(hours, rate, bonus=0):
    try:
        return (float(hours)*float(rate))+float(bonus)
    except ValueError:
        return 'Wrong value type'


def main(argv_list):
    try:
        keys = argv_list[1::2]
        values = argv_list[2::2]
        kwargs = dict(zip(keys, values))
        print(calc_salary(**kwargs))
    except TypeError:
        print('Expects two mandatory parameters: hours, rate and one optional: bonus')


if __name__ == '__main__':
    from sys import argv
    main(argv)
