"""
Задача 4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


def main():
    from functools import reduce
    while True:
        try:
            user_input = abs(int(input('Please enter positive integer number: ')))
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    result = reduce(
        lambda a, b: int(a) if int(a) > int(b) else int(b),
        str(user_input)
    )
    print(f'Result is: {result}')


if __name__ == '__main__':
    main()
