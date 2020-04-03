"""
Задача 6
*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию
об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара:
название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у
пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""


def main():
    products = list()

    def create_product(name, price, quantity, unit):
        return (
            len(products)+1,
            {
                'name': name,
                'price': price,
                'quantity': quantity,
                'unit': unit,
            },
        )

    while True:
        print('Creating new Product.')
        try:
            product = create_product(
                name=input('Enter product name: '),
                price=abs(int(input('Enter product price: '))),
                quantity=abs(int(input('Enter product quantity: '))),
                unit=input('Enter product units: '),
            )
            products.append(product)
            if input('Type "y" to add another: ') == 'y':
                continue
            break
        except ValueError:
            print('Wrong value. Try again.')

    statistics = {
        'name': set(),
        'price': set(),
        'quantity': set(),
        'unit': set(),
    }

    for product in products:
        values = product[1]
        for (key, val) in statistics.items():
            if type(val) is set and type(values) is dict:
                val.add(values[key])

    print('Statistics: ')
    for (key, val) in statistics.items():
        print(f'{key}: {str(val).strip("{}")}')


if __name__ == '__main__':
    main()
