"""
Задача 5
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""


def main():
    earnings = None
    expenses = None
    while True:
        try:
            if earnings is None:
                earnings = round(abs(float(input('Tell me your company\'s earnings (must be positive float): '))), 2)
            if expenses is None:
                expenses = round(abs(float(input('Tell me your company\'s expenses (must be positive float): '))), 2)
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    profit = round(earnings-expenses, 2)
    is_profitable = profit > 0
    if is_profitable:
        print(f'Your company is profitable. Your profit is: {profit}')
    else:
        print('Your company is NOT profitable.')
    while True:
        try:
            employees = abs(int(input('How many people work for you (positive integer): ')))
            break
        except ValueError:
            print('Wrong value.\nTry again.')
    profit_per_employee = round((profit/employees), 2)
    print(f'Profit per employee: {profit_per_employee}')


if __name__ == '__main__':
    main()
