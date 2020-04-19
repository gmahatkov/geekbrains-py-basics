"""
Задача 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут
реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на
ваше усмотрение.  Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт.
"""
from enum import Enum
from time import sleep
from itertools import cycle


class TrafficLight:
    class Color(Enum):
        RED = 1
        YELLOW = 2
        GREEN = 3

    __color = Color.GREEN

    __colors_map = {
        Color.RED: 7,
        Color.YELLOW: 2,
        Color.GREEN: 5,
    }

    def running(self):
        try:
            for color in cycle(self.Color):
                self.__color = color
                print('Now color is: ', str(self.__color.name))
                sleep(self.__colors_map[color])
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    traffic_light = TrafficLight()
    traffic_light.running()

