try:
    age = int(input("Введите ваш возраст: "))
    citizen = input("Гражданин? (да/нет): ").strip().lower() == "да"
    the_criminal = input("Есть уголовное наказание? (да/нет): ").strip().lower() == "да"

    if age >= 18 and citizen and not the_criminal:
        print("✓ Может голосовать")
    else:
        print("✗ Не может голосовать")

except ValueError:
    print("Ошибка: возраст должен быть числом!")