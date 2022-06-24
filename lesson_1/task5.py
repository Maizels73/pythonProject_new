"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
6. Если фирма отработала с прибылью, вычислите рентабельность выручки. Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
"""
revenue = int(input("Enter revenue:  "))
expense = int(input("Enter expense:  "))

if revenue > expense:
    works = int(input("Enter workers:  "))
    profit = revenue - expense
    ren = 100 * profit / expense
    salary = profit * 16 / 100 / works
    print(f"Your profit = {profit} Your rentability = {ren}|| workers' salary = {salary}")
else:
    if revenue == expense:
        print(f" все печально, работаем в нуль")
    else:
        print(f" все плохо, без комментариев")
