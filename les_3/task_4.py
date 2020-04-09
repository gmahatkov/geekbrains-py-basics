"""
Задача 4
Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение
числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо
обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй —
более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    return x ** y


def main():
    while True:
        try:
            x = abs(float(input('Positive float')))
            y = int(input('Integer: '))
            print(f'Result: {my_func(x, y)}')
            break
        except ValueError:
            print('Wrong value. Try again.')


if __name__ == '__main__':
    main()