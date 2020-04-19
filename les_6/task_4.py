"""
Задача 4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
вызов методов и также покажите результат.
"""
from enum import Enum


class Color(Enum):
    BLACK = 'black'
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    YELLOW = 'yellow'


class Direction(Enum):
    F = 'forward'
    B = 'backward'
    L = 'left'
    R = 'right'


class Car:
    __last_turn_direction = None

    def __init__(self, speed=0, color=Color.BLACK, name='', is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Going')
        self.speed += 10

    def stop(self):
        print('Stop')
        self.speed = 0

    def turn(self, direction):
        if direction not in Direction:
            raise ValueError()
        if self.__last_turn_direction == direction:
            self.go()
            return
        self.__last_turn_direction = direction
        self.speed = self.speed-10 if self.speed > 10 else 0

    def show_speed(self):
        print(f'{self.name}: Current speed is: {self.speed}')


class TownCar(Car):
    def __init__(self, color):
        super().__init__(color=color, name='Town Car')

    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name}: Too fast!')
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, color):
        super().__init__(color=color, name='Sport Car')


class WorkCar(Car):
    def __init__(self, color):
        super().__init__(color=color, name='Work Car')

    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name}: Too fast!')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color):
        super().__init__(color=color, name='Police Car', is_police=True)


if __name__ == '__main__':
    town_car = TownCar(Color.BLUE)
    work_car = WorkCar(Color.RED)
    sport_car = SportCar(Color.YELLOW)
    police_car = PoliceCar(Color.BLACK)
    cars = [town_car, work_car, sport_car, police_car]
    for car in cars:
        for i in range(5):
            car.go()
            car.turn(Direction.L)
            car.go()
            car.turn(Direction.R)
            car.go()
            car.turn(Direction.R)
            car.go()
            car.show_speed()

