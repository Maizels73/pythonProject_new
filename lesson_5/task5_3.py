"""
3. Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
 Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
 Выполнить подсчёт средней величины дохода сотрудников.

Пример файла:
"""
with open("task5_3.txt", encoding='utf-8') as fl:
    my_list = fl.readlines()
    nb_str = ""
    count_str = 0
    all_sum = 0
    for str_content in my_list:

        fio = str_content.split()[0]
        zp = int(str_content.split()[1])
        all_sum = all_sum + zp
        count_str += 1
        if zp < 2000:
            nb_str = f"{fio} - {zp}\n{nb_str}"

    print(f'среднее по больнице = {all_sum / count_str} ')
    if nb_str != "":
        print(f'список бедолаг\n{nb_str}')
    else:
        print("нищебродов не держим")
