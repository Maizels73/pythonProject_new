"""
2. Пользователь вводит время в секундах.
 Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
get_time = int(input('enter time in seconds: '))
get_hour = get_time // 3600
get_min = get_time // 60 - get_hour * 60
get_sek = get_time % 60
print(f"{get_hour:02}:{get_min:02}:{get_sek:02}")
