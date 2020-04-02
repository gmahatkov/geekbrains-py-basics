"""
Задача 2
Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


def parse_time(time):
    return f'0{str(time)}' if len(str(time)) < 2 else str(time)


def main():
    while True:
        try:
            seconds_input = abs(int(input('Enter number of seconds (must be integer): ')))
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    s = parse_time(int(seconds_input % 60))
    m = parse_time(int((seconds_input/60) % 60))
    h = parse_time(int(seconds_input/3600))
    print(f'Parsed time: {h}:{m}:{s}')


if __name__ == '__main__':
    main()
