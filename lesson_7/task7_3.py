"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
"""


class Cell:
    num_in_row = 7

    def __init__(self, nucleus):
        if nucleus > 0:
            self.nucl = nucleus
        else:
            raise ValueError("nucleus is negative or null")

    def __add__(self, other):
        k = Cell(self.nucl + other.nucl)
        return f"result of addition:{self.nucl} + {other.nucl} = {self.nucl + other.nucl} \n{k.make_order()}"

    def __sub__(self, other):
        k = Cell(self.nucl - other.nucl)
        return f"result of subtraction:{self.nucl} - {other.nucl} = {self.nucl - other.nucl} \n{k.make_order()}"

    def __mul__(self, other):
        k = Cell(self.nucl * other.nucl)
        return f"result of multiplication:{self.nucl} * {other.nucl} = {self.nucl * other.nucl} \n{k.make_order()}"

    def __truediv__(self, other):
        k = Cell(self.nucl // other.nucl)
        return f"result of divided:{self.nucl} // {other.nucl} = {self.nucl // other.nucl} \n{k.make_order()}"

    def make_order(self):
        list_str = ""
        rest = self.nucl

        while rest > 0:
            rest = rest - Cell.num_in_row
            if rest >= 0:
                list_str = list_str + ("*" * Cell.num_in_row) + "\n"
            else:
                list_str = list_str + "*" * (Cell.num_in_row + rest)
                list_str = list_str + "-" * abs(rest)
        return list_str


cell1 = Cell(13)
cell2 = Cell(3)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
