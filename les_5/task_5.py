"""
Задача 5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна
подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from os import path, getcwd
from random import randint


def main():
    f_name = path.join(getcwd(), 'task_5_test')
    nums = [i * randint(1, 70) for i in range(1, randint(10, 21))]
    print('Nums: ', str(nums).strip('[]'))
    with open(f_name, 'w+') as f:
        f.write(','.join(map(str, nums)))
    with open(f_name, 'r') as f:
        nums = f.read().split(',')
        print('Sum: ', sum(map(int, nums)))


if __name__ == '__main__':
    main()
