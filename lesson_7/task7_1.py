"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.


Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, matrix):
        self.mat = matrix

    def __str__(self):
        s = ""
        for line in self.mat:
            s += " ".join([str(x) for x in line]) + "\n"
        return s

    def __add__(self, other):
        if len(self.mat) == len(other.mat) and len(self.mat[0]) == len(other.mat[0]):
            result = [[0 for _ in range(len(self.mat[0]))] for _ in range(len(self.mat))]
            for i in range(len(self.mat)):
                for j in range(len(self.mat[i])):
                    k = self.mat[i][j]
                    l = other.mat[i][j]
                    result[i][j] = k + l
        return Matrix(result)

        return f"ERROR! matrices are not identical"


m = Matrix([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])
n = Matrix([[2, 2], [2, 2], [2, 2], [2, 2], [2, 2]])
#n1 = Matrix([[3, 3], [3, 3], [3, 3], [3, 3], [3, 3]])
k = m + n
print(f"{m} + ")
print(f"{n} = ")
print(f"{k}")
#print (type(k))
