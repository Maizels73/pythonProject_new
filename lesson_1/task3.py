"""
3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
get_num = input("Enter number > 0:  ")
get_num_int = int(get_num)
if get_num_int <= 0:
    print("The number <=0 try again")
else:
    num1 = int(get_num + get_num)
    num2 = int(get_num + get_num + get_num)
    print(f"{get_num} + {num1} + {num2} = {get_num_int + num1 + num2}")
