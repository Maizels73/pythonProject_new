"""
Реализовать функцию my_func(), которая принимает три позиционных
аргумента и возвращает сумму наибольших двух аргументов.
"""


def my_func(num_1, num_2, num_3):
    try:
        my_list = list(map(float, [num_1, num_2, num_3]))
        my_list.remove(min(my_list))
        print(my_list)
        return sum(my_list)
    except (TypeError, ValueError):
        return "Error"


print(my_func(float(input(f" введите первое число ")),
              float(input(f" введите второе число ")),
              float(input(f" введите тертье число "))))
