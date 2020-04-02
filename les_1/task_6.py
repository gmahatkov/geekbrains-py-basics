"""
Задача 6
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена
составит не менее b километров. Программа должна принимать значения параметров a и b и  выводить одно натуральное
число — номер дня.
Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""


def main():
    a = None
    b = None
    while True:
        try:
            if a is None:
                a = abs(int(input('Enter first day achievement (must be positive integer): ')))
            if b is None:
                b = abs(int(input('Enter desired achievement (must be positive integer): ')))
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    counter = 1
    while a < b:
        a = round(a * 1.1, 2)
        counter += 1
    print(f'To achieve the result of {b}km you need at least: {counter} days')


if __name__ == '__main__':
    main()
