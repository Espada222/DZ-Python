try:
    num = int(input("Введите число от 1 до 5: "))

    if num == 1:
        text = "One"
    elif num == 2:
        text = "Two"
    elif num == 3:
        text = "Three"
    elif num == 4:
        text = "Four"
    elif num == 5:
        text = "Five"
    else:
        print(f"Ошибка: число {num} не входит в диапазон от 1 до 5. Программа завершена.")
        text = None

    if text:
        print(f"Соответствующее число: {text}")

except ValueError:
    print("Ошибка: введите целое число. Программа завершена.")