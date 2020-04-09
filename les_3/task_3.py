"""
Задача 3
Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""
from functools import reduce


def my_func(*args):
    try:
        nums = list(map(float, args))
        nums.sort(reverse=True)
        return reduce(lambda a, b: a+b, nums[:2])
    except ValueError:
        print('Got arguments of wrong type. Expect float.')


def main():
    while True:
        args = tuple(input('Enter at least three nums: ').split())
        if len(args) < 3:
            print(f'Expect at least three numbers got: {len(args)}')
            continue
        result = my_func(*args)
        if result is not None:
            print(f'Result: {result}')
            break
        print('Something went wrong. Try again.')


if __name__ == '__main__':
    main()
