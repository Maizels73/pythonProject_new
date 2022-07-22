"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class My_data:
    def __init__(self, text):
        self.text = text

    @classmethod
    def get_data(cls,dan):
        data_str = dan.split("-")
        data_list = []
        for i in range(0, len(data_str)):
            try:
                data_list.append(int(data_str[i]))
            except ValueError:
                err = True
        return (data_list)

    @staticmethod
    def is_valid(num):
        err = ""
        if len(num)!=3:
            return ("Common Error")
        else:

         if num[0] <= 0 or num[0] > 31:
          err = "Error in day"
         if num[1] <= 0 or num[1] > 12:
          err = err + " Error in month"

         if err == "":
            return f"Good data: {num[0]}-{num[1]}-{num[2]}"
         else:
            return (err)




first = My_data(input(" введите дату в формате день-месяц-год: "))
data_list = (My_data.get_data(first.text))
print(My_data.is_valid(data_list))




