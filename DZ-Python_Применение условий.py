summa = 0
for i in range(2, 101, 2):
    summa += i
print("Сумма:", summa)

squares = [x ** 2 for x in range(1, 11) if x % 2 != 0]
print("Список:", squares)

count = 0
while True:
    try:
        number = float(input("Введите число (отрицательное — для выхода): "))
    except ValueError:
        print("Ошибка: введите корректное число!")
        continue
    if number < 0:
        break
    count += 1
print("Количество введенных чисел:", count)