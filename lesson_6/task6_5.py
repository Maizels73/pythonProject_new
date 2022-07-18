"""
 Реализовать класс Stationery (канцелярская принадлежность).

    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:

 def __init__(self, title):
    self.title = title

 def my_metod(self):
        print (f"{self.title}")

class Pen(Stationery):
    def my_metod(self):
        print(f"ручки типа {self.title}")

class Pencil(Stationery):
    def my_metod(self):
        print(f"карандаша типа {self.title}")

class Marker(Stationery):
    def my_metod(self):
        print(f"маркера типа {self.title}")


start = Stationery("Начинаем рисовать с помощью:")
pen = Pen("ручки №1")
penc = Pencil("карандаша №2")
mark = Marker("маркера №3")

start.my_metod()
pen.my_metod()
penc.my_metod()
mark.my_metod()


