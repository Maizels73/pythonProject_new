"""
 Программа запрашивает у пользователя строку чисел, разделённых пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
 Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def sum_num():
    sum = 0
    er_list = []
    while True:
        err = False
        in_list = input("введите числа выход: q: ").split()
        for num in in_list:
            if num.lower() == "q":
                if err:
                    print(f"Error {er_list}")
                return f" EXIT result = {sum}"
            else:
                try:
                    sum = sum + int(num)
                except ValueError:
                    err = True
                    er_list.append(num)
        if err:
            print(f"Error {er_list}")
        print(f"Sum of numbers = {sum}")


print(sum_num())
