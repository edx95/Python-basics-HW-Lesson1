# ДЗ_1.2

# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours:02} :  {minutes:02} : {seconds:02}")

time = int(input("Введите время в секундах: "))
hours = time // 3600
ostatok = time % 3600
minutes = ostatok // 60
seconds = ostatok % 60
print(f"Время в секундах {hours:02}:{minutes:02}:{seconds:02}")