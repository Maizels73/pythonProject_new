"""
1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

my_fl = open("task5_1.txt", 'w', encoding='utf-8')
my_stop = 1
while my_stop !=0:
    my_tekst = input(f" enter text")
    if my_tekst == "":
        my_stop = 0
        my_fl.close()
    else:
        my_fl.write(f"{my_tekst}\n")



