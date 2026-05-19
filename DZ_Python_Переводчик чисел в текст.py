try:
    num = int(input("Введите число от 1 до 5: "))
    numbers = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five"
    }
    if num in numbers:
        print(f"Соответствующее число: {numbers[num]}")
    else:
        print(f"Ошибка: число {num} не входит в диапазон от 1 до 5")
except ValueError:
    print("Ошибка: введите целое число. Программа завершена.")
