"""
Задача 2
Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
использовать функцию input().
"""


def main():
    original = list()
    while True:
        original.append(input('Enter something: '))
        while True:
            append_more = input('Do you want to append more elements? (y/n): ')
            if append_more in ['y', 'n']:
                break
        if append_more == 'n':
            break
    processed = list()
    print('Original list:')
    for idx, cur in enumerate(original):
        print(f'{idx}. {cur}')
        if idx > 0 and idx % 2 > 0:
            prev = original[idx-1]
            processed.extend([cur, prev])
        if idx == len(original)-1:
            processed.append(cur)
    print('Processed list:')
    for idx, item in enumerate(processed):
        print(f'{idx}. {item}')


if __name__ == '__main__':
    main()
