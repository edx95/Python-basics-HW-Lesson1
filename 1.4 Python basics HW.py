# ДЗ_1.4
#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#V1
a = int(input('Введите целое положительное число: '))
n = a%10
a = a//10
while a > 0:
    if a%10 > n:
        n = a%10
    a = a//10
print(f"Самая большая цифра в числе {n}")

#V2
number = int(input("Введите целое положительное число: "))
max = number % 10
while number >= 1:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    if number > 9:
        continue
    else:
        print("Самая большая цифра в числе: ", max)


#V3
a = int(input('Введите целое положительное число: '))
m = a % 10
a = a // 10
while a > 0:
    if a % 10 > m:
        m = a % 10
    a = a // 10
print("Самая большая цифра в числе: ", m)


#V4
number = int(input('Введите целое число: '))
max = number % 10
num = number

while num > 0:
    digit = num % 10
    if digit > max:
        max = digit

    if digit == 9:
        break

    num //= 10
    print(num)
print(f"Наибольшая цифра в числе {number} равна {max}")
