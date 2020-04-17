"""
Задача 6
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                                        Физика:   30(л)   —   10(лаб)
                                        Физкультура:   —   30(пр)   —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
from os import path, getcwd
from re import sub


def main():
    f_name = path.join(getcwd(), 'task_6_test')
    result = dict()
    if path.exists(f_name):
        with open(f_name, 'r') as f:
            try:
                for line in f.readlines():
                    name, *nums = line.split()
                    nums = [int(i) for i in map(lambda s: sub(r'[^\d]', '', s), nums) if len(i) > 0]
                    result[name] = sum(nums)
            except ValueError as e:
                print(e)
                pass
    print(result)


if __name__ == '__main__':
    main()
