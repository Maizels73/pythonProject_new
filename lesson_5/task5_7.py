'''
7. Создать вручную и заполнить несколькими строками текстовый файл,
 в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
'''
import json
my_dict = {}
i = 0
sum = 0
with open("my_ex7.json", "w", encoding="utf-8") as new_f, open("task5_7.txt", encoding="utf-8") as fl:
    for firm in fl:
        firm_name = firm.split(" ")[0]
        firm_info = firm.split(" ")[1]
        firm_dohod = int(firm.split(" ")[2])
        firm_rashod = int(firm.split(" ")[3])
        firm_rent = firm_dohod - firm_rashod
        my_dict[firm_name] = firm_rent
        if firm_rent >= 0:
            sum = sum + firm_rent
            i +=1
        aver = [sum / i]
      #  print(my_dict)
      #  print(type(my_dict))
        json.dump(aver, new_f, ensure_ascii=False, indent=4)