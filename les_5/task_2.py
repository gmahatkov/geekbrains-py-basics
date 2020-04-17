"""
Задача 2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества
слов в каждой строке.
"""
from os import path, getcwd


def main():
    f_name = path.join(getcwd(), 'task_2_test')
    if path.exists(f_name):
        with open(f_name, newline='') as f:
            lines = f.readlines()
            for line_idx, line in enumerate(lines, 1):
                print(f"{line_idx} ; line length: {len(line.split())} ; {line}")
            print(f'Total: {len(lines)}')


if __name__ == '__main__':
    main()
