"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
get_num = int(input("Enter number > 0:  "))
max_digit = 0
now_digit = 0
if get_num <= 0:
    print("The number <=0 try again")
else:
    while get_num > 0:
        now_digit = get_num % 10
        # print (f"get_num= {get_num}|| max_digit= {max_digit} || now_digit= {now_digit}")
        if now_digit >= max_digit:
            max_digit = now_digit
        get_num = get_num // 10

print(f" max_digit= {max_digit}")
