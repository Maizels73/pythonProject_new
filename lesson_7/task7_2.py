"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
 для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
 абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = "Одежда"
    common_rashod = 0

    @property
    @abstractmethod
    def rashod(self):
        pass

    @abstractmethod
    def __del__(self):
        pass


class Suit(Clothes):

    def __del__(self):
        Clothes.common_rashod -= self.rashod

    def __init__(self, height: float):
        self.ht = height
        Clothes.common_rashod += self.rashod

    @property
    def rashod(self):
        return round(self.ht * 2 + 0.3, 2)


class Coat(Clothes):

    def __del__(self):
        Clothes.common_rashod -= self.rashod

    def __init__(self, body_size):
        self.bs = body_size
        Clothes.common_rashod += self.rashod

    @property
    def rashod(self):
        return round(self.bs / 6.5 + 0.5, 2)


if __name__ == '__main__':
    suit1 = Suit(1.5)
    coat1 = Coat(54)
    coat2 = Coat(54)

    print(suit1.rashod)
    print(coat1.rashod)
    print(coat2.rashod)
   # print(suit1.rashod + coat1.rashod)

    print(Clothes.common_rashod)
    del (coat2)
    print(Clothes.common_rashod)
