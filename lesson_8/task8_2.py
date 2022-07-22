"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
 При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivZero(Exception):
    def __init__(self, txt_eror):
        self.txt_eror = txt_eror


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    if num2 == 0:
        raise DivZero("На ноль у нас не делят")
except ValueError:
    print("такое не делим")
except DivZero as err:
    print(f"{err} + !!!")
else:
    print(num1 / num2)
