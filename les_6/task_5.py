"""
Задача 5
Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__.lower()

    def draw(self):
        print(f'Start drawing with {self.title}.')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


if __name__ == '__main__':
    classes = [Pen, Pencil, Handle]
    instances = [cls() for cls in classes]
    for instance in instances:
        instance.draw()
