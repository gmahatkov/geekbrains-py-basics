"""
Задача 2
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def main():
    from random import randint
    original = [randint(1, 500) for i in range(15)]
    print('Original: ', str(original).strip('[]'))
    processed = [a for idx, a in enumerate(original) if idx > 0 and a > original[idx-1]]
    print('Processed: ', str(processed).strip('[]'))


if __name__ == '__main__':
    main()
