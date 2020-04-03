"""
Задача 5
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""


def main():
    from random import randint
    rates = [randint(1, 10) for i in range(1, randint(1, 10))]
    rates.sort(reverse=True)
    print(f'Original list: {str(rates).strip("[]")}')
    user_rates = list()
    while True:
        try:
            user_input = abs(int(input('Enter any natural number in range of 1 to 10: ')))
            if user_input > 10 or user_input == 0:
                raise ValueError
            user_rates.append(user_input)
            add_more = input('Do you want to add more? (y/n)')
            if add_more == 'y':
                continue
            break
        except ValueError:
            print('Wrong value. Try again.')
    rates.extend(user_rates)
    rates.sort(reverse=True)
    print(f'Result: {str(rates).strip("[]")}')
    pass


if __name__ == '__main__':
    main()
