"""
Задача 5
Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа
от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


def main():
    from functools import reduce
    my_list = [i for i in range(100, 1000, 2)]
    result = reduce(lambda a, b: a+b, my_list)
    print('Result: ', result)


if __name__ == '__main__':
    main()