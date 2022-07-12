"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

from random import randint
fl = open("task5_5.txt", "w")
fl.write(" ".join([str(randint(1, 100)) for _ in range(10)]))
fl.close()
fl = open("task5_5.txt")
print(sum(map(int, fl.readline().split())))