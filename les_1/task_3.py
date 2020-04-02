"""
Задача 3
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


def main():
    from functools import reduce
    while True:
        try:
            n = abs(int(input('Please enter any positive integer number: ')))
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    values = [int(str(n)*idx) for idx in range(1, 4)]
    result = reduce(
        lambda a, b: a+b,
        values
    )
    print(f'Result: {result}')


if __name__ == '__main__':
    main()
