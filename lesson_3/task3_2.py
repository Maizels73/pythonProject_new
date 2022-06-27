"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def people_info(name, surname, year_b, town_l, email, tel):
    str = f"name: {name}, surname={surname}, year_b={year_b}, town_l={town_l}, email={email}, tel={tel}"
    return str


res_people_info = people_info(name=input("Введите имя: "),
                              surname=input("Введите фамилию: "),
                              year_b=input("Введите год рождения: "),
                              town_l=input("Введите город проживания: "),
                              email=input("Введите e-mail: "),
                              tel=input("Введите телефон: "))
print(res_people_info)
