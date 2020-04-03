"""
Задача 3
Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
лето, осень). Напишите решения через list и через dict.
"""


def main():
    while True:
        try:
            month = abs(int(input('Enter number between 1 to 12: ')))
            if month > 12:
                raise ValueError
            break
        except ValueError:
            print('Wrong value. Try again.')
    seasons = {
        (12, 1, 2): 'winter',
        range(3, 6): 'spring',
        range(6, 9): 'summer',
        range(9, 12): 'fall'
    }
    month_names = [
        'JAN',
        'FEB',
        'MAR',
        'APR',
        'MAY',
        'JUN',
        'JUL',
        'AUG',
        'SEP',
        'OCT',
        'NOV',
        'DEC',
    ]
    for (key, name) in seasons.items():
        if month in key:
            print(f'It\'s {name} time! it\'s {month_names[month-1]} outside!')
            break


if __name__ == '__main__':
    main()
