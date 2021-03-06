"""
Задача 4
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""


def main():
    from random import randint
    original = [randint(1, 20) for i in range(1, 15)]
    print('Original: ', str(original).strip('[]'))
    result = [i for i in original if original.count(i) == 1]
    print('Result: ', str(result).strip('[]'))


if __name__ == '__main__':
    main()
