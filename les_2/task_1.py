"""
Задача 1
Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""


def main():
    my_list = [42, '42', 42.42, True, None]
    my_list.append(my_list)
    for item in my_list:
        print(type(item))


if __name__ == '__main__':
    main()
