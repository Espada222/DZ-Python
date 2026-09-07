password = "Qwerty123"

user_input = ""

while user_input != password:
    user_input = input("Введите пароль:")

    if user_input == password:
        print("Верный пароль")
    else:
        print("Неверный пароль")