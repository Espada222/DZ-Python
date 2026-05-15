while True:
    try:
        num = int(input("Введите число от 0 до 5: "))

        if 0 <= num <= 5:
            print(f"Обратный отсчёт от {num} до 0:")
            while num >= 0:
                print(num)
                num -= 1
            break
        else:
            print("Ошибка: число должно быть в диапазоне от 0 до 5. Попробуйте снова.")

    except ValueError:
        print("Ошибка: введите целое число. Попробуйте снова.")