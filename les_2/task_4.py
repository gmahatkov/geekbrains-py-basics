"""
Задача 4
Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""


def main():
    from re import search
    while True:
        try:
            sentence = input('Enter any sentence (more then one word required): ')
            if len(sentence) == 0 or search(r'\w\s\w', sentence) is None:
                raise ValueError
            break
        except ValueError:
            print('Wrong value. Try again.')
    print('Result: ')
    for idx, word in enumerate(sentence.split(), 1):
        print(f'{idx} - {word}')


if __name__ == '__main__':
    main()
