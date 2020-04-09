"""
Задача 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_div(a, b):
    try:
        return float(a) / float(b)
    except ValueError:
        print(f'Arguments of wrong type. Expect type int, got: {type(a)} and {type(b)}')
    except ZeroDivisionError:
        print('Second argument must not be 0.')


def main():
    while True:
        try:
            a, b = input('Enter two numbers divided by space: ').split()[:2]
            result = my_div(a, b)
            if result is not None:
                print(f'Result: {result}')
                break
            print('Something went wrong. Try again.')
        except ValueError:
            print('Expect two arguments got 1.')


if __name__ == '__main__':
    main()
