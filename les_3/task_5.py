"""
Задача 5
Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел
будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
полученной ранее сумме и после этого завершить программу.
"""
from functools import reduce


def create_acc_fn():
    acc = 0

    def acc_fn(*args):
        nonlocal acc
        result = 0
        try:
            escape_sign_idx = list(args).index('/')
        except ValueError:
            escape_sign_idx = None
        try:
            nums = list(map(float, args[:escape_sign_idx]))
            result = reduce(lambda a, b: a+b, nums, acc)
            acc = result if escape_sign_idx is None else 0
        except ValueError as e:
            print(e)
        return result
    return acc_fn


def main():
    acc_fn = create_acc_fn()
    while True:
        args = tuple(
            input('Enter numbers divided by space or symbol "/" to reset accumulator or press Enter to quit: ').split()
        )
        if len(args) == 0:
            break
        print(f'Current result: {acc_fn(*args)}')


if __name__ == '__main__':
    main()
