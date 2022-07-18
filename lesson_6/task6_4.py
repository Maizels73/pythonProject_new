"""
 Реализуйте базовый класс Car.

    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
    turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько
    дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed,
    который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод
    show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
    скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, nm, col, spd, pol=False):
        self.name = nm
        self.color = col
        self.speed = spd
        self.is_police = pol
        print(f'The car is: {nm}  color: {col}.Police - {pol}')

    def go(self):
        print(f'{self.name}: Now go')

    def stop(self):
        print(f'{self.name}: Now Stop')

    def turn(self, to_dir):
        print(f'{self.name}: Now turn to {to_dir}.')

    def show_speed(self):
        print(f'{self.name}: Now speed: {self.speed}.')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name}: Car speed: {self.speed}. Speed high' if self.speed > 60 else super().show_speed())


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name}: Car speed: {self.speed}. Speed high' if self.speed > 40 else super().show_speed())


class SportCar(Car):
    """SportCar"""


class PoliceCar(Car):

    def __init__(self, nm, col, spd):
        super().__init__(nm, col, spd, pol=True)


police_car = PoliceCar("PoliceCar", 'black', 80)
work_car = WorkCar("WorkCar", 'white', 111)
sport_car = SportCar("SportCar", 'yellow', 120)
town_car = TownCar("TownCar", 'red', 222)
police_car.go()
police_car.show_speed()
police_car.turn("left")
police_car.stop()
print()
work_car.go()
work_car.show_speed()
work_car.turn("right")
work_car.stop()
print()
sport_car.go()
sport_car.show_speed()
sport_car.turn("right")
sport_car.stop()
print()

town_car.go()
town_car.show_speed()
town_car.turn("right")
town_car.stop()
