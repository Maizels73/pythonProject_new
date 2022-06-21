"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
У пользователя нужно запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
"""
my_list = [123, 121, 121, 80, 77, 77, 7, 7, 7, 5, 5, 4, 3, 3, 3, 1]
num = int(input("введите любое число: "))
new_index = "none"
len_list = len(my_list)
if num > max(my_list):
    new_index = 0
if num < min(my_list):
    new_index = len_list
nal = my_list.count(num)
if nal != 0:
    index_num = my_list.index(num)
    if index_num + 1 == len_list:
        new_index = len_list
    else:
        next_index = index_num + 1
        while next_index < len_list:
            if num != my_list[next_index]:
                new_index = next_index
                break
            else:
                next_index = next_index + 1

if new_index == "none":
    i = 0
    while i < len_list:
        if num > my_list[i]:
            new_index = i
            break
        i = i + 1

copy_list = my_list.copy()
copy_list.insert(new_index, num)
print(my_list)
print(copy_list)
