# ДЗ_1.6
#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

#V1

a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)







#V2
while True:
    days = 1
    start_km = float(input('Начальный результат:'))
    last_km = float(input('Финальный результат:'))
    if start_km <= 0 or last_km < 0:
        print('Результаты должны быть больше нуля! Стартовое значение != 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
        print(f'Спортсмен добьтся результата за {days} дней')

