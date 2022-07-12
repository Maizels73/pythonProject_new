"""
4. Создать (не программно) текстовый файл со следующим содержимым:

One — 1
Two — 2
Three — 3
Four — 4

"""
rus_num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("task5_4.txt", encoding='utf-8') as fl:
    my_list = fl.readlines()
    new_str = ""
    for str_content in my_list:
        txt_num = str_content.split("-")[0]
        txt_num = txt_num.split()[0]
        int_num = str_content.split("-")[1]
        new_n = rus_num.get(f"{txt_num}")
        new_str = f"{new_str}\n {new_n} - {int_num}"

    print(new_str)
with open("task5_4_new.txt", "w", encoding='utf-8') as new_file:
    new_file.write(new_str)