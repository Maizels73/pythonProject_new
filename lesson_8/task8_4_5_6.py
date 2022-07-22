"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве
единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

from abc import ABC, abstractmethod


class StorageFullException(Exception):
    def __str__(self):
        return "Склад заполнен!"


class NotIdException(Exception):
    def __init__(self, not_id):
        self.not_id = not_id

    def __str__(self):
        return f"Экземпляра по id {self.not_id}  нет!"


class Sklad:
    def __init__(self, max_count, name, dir_fio):
        self.max_count = max_count
        self.name = name
        self.dir_fio = dir_fio
        self._store = {}

    def priem(self, obj):
        if len(self._store) < self.max_count:
            self._store[obj.id] = obj
        else:
            raise StorageFullException()

    def vidacha(self, serch=None):

        if serch is None:
            return "None"
        else:
            if serch in self._store:
                return self.store.pop(serch)
            else:
                raise NotIdException(serch)

    @property
    def store(self):
        return self._store

    def priem_list(self, lst):
        # self._store.extend(objs)
        i = len(lst)
        try:
            for obj in lst:
                self.priem(obj)
                i -= 1
        except StorageFullException as ex:
            print(f"{ex} - {i} из {len(lst)} не влезло - склад не резиновый max = {self.max_count}")


class OrgTex(ABC):
    id_current = 0
    er_in = 0

    def __init__(self, model="", price=0.00):
        self.model = model
        self.price = price
        self.id = OrgTex.id_current
        OrgTex.id_current += 1

    def __repr__(self):
        return f"{self.__class__.__name__} id: {self.id} model: {self.model} price: {self.price}"

    @staticmethod
    def build(col: int, cls: type, *args):
        """ Создает col - объектов cls - класса """
        return [cls(*args) for _ in range(col)]

    @classmethod
    @abstractmethod
    def inp(cls):
        in_mod = input(f"Введите модель {cls.__name__} ")
        in_price = float(input(f"Введите стоимость {cls.__name__} "))
        return in_mod, in_price


class Printer(OrgTex):
    @classmethod
    def inp(cls):
        try:
            in_mod, in_price = super().inp()
            in_tp = input(f"Введите тип  {cls.__name__}")
            in_color = bool(input(f" {cls.__name__} - цветной/ ЧБ (1/0)"))
            return Printer(in_mod, in_price, in_tp, in_color)
        except ValueError as ex:
            print(ex)

    def __init__(self, model, price, type_pr, is_color_pr):
        super().__init__(model, price)
        self.type_pr = type_pr
        self.is_color_pr = is_color_pr


class Telefon(OrgTex):
    @classmethod
    def inp(cls):
        in_mod, in_price = super().inp()
        in_tp = input(f"Введите тип  {cls.__name__} ")
        in_color = bool(input(f"{cls.__name__} - операционная система "))
        return Printer(in_mod, in_price, in_tp, in_color)

    def __init__(self, model, price, type_tel, os):
        super().__init__(model, price)
        self.type_tel = type_tel
        self.os = os


if __name__ == '__main__':
    sk1 = Sklad(10, "Sklad", "Ivanov I.")
    sk2 = Sklad(10, "Sklad2", "Petrov I.")

    pr1 = Printer.inp()
    sk2.priem(pr1)

    tl1 = Telefon.inp()
    sk1.priem(tl1)

    printers = OrgTex.build(5, Printer, "HP 1212", 10000, "Laser", False)
    tels = OrgTex.build(5, Telefon, "Nokia 3010", 12000, "cell", "nokia_os")

    sk1.priem_list(printers)
    sk2.priem_list(tels)

    print("\nСостояние на момент заполнения складов\n")
    print(f" Склад1 {sk1.store}")
    print(f" Склад2 {sk2.store}")

    try:
        sk2.priem(sk1.vidacha(222))
    except NotIdException as ex:
        print(f"{ex}")

    try:
        sk1.priem(sk2.vidacha(6))
    except NotIdException as ex:
        print(f"{ex}")

    print("\nСостояние на после выдачи\n")
    print(f"Склад1 {sk1.store}")
    print(f"Склад2 {sk2.store}")
