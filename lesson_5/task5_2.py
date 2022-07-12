"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""
with open("task5_2.txt", encoding='utf-8') as fl:
    my_line = fl.readlines()
    for num, str_content in enumerate(my_line, 1):
        count_wr = len(str_content.split())
        str_fl = str_content.split()
        print(f'{str_fl} = {count_wr} слов')
    print(f"Всего {num} строк")
