"""
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text.
7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""
def int_func():
    str = ""
    word_list = ""
    er_dict = {}
    err = 0
    for word in input("Введите набор слов:\n").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                err = err
            else:
                err = True
                str = f"{str}|{char}"
                er_dict.update({word: str})
        if not err:
            word_list = f"{word_list} {word.title()}"
        err = 0
        str = ""

    print(word_list)
    print(er_dict)


int_func()
