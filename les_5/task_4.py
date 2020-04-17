"""
Задача 4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
from os import path, getcwd


def main():
    translations = {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
    }
    src_f_name = path.join(getcwd(), 'task_4_test_src')
    dst_f_name = path.join(getcwd(), 'task_4_test_dst')
    if path.exists(src_f_name):
        with open(src_f_name, newline='', mode='r') as f:
            txt = f.read()
            for key, val in translations.items():
                txt = txt.replace(key, val)
        with open(dst_f_name, 'w') as f:
            f.write(txt)


if __name__ == '__main__':
    main()
