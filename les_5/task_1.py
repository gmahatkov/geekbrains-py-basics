"""
Задача 1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
ввода данных свидетельствует пустая строка.
"""
from os import path, getcwd


def main():
    f_name = path.join(getcwd(), 'task_1_test')
    with open(f_name, "w") as f:
        while True:
            user_input = input("Enter something or leave blank to quit: ")
            if len(user_input) > 0:
                f.write(f'{user_input}\n')
            else:
                break


if __name__ == '__main__':
    main()
