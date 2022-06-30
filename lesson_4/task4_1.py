"""
task4_1
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def my_salar(name, hours, stavka, bonus):
    try:
        salary = int(hours) * float(stavka) + int(bonus)
        print(f" ЗП + бонус = {salary}")
    except ValueError:
        print(f" ERROR PARAMETRS OF IMPUT")


try:
    name, n_1, n_2, n_3 = argv
    my_salar(name, n_1, n_2, n_3)
except ValueError:
    print(f" ERROR INPUT")

