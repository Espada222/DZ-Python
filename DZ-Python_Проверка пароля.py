password = "Qwerty123"

while True:
    user = input("Введите пароль:")

    if user == password:
        print("Верный пароль")
        break
    else:
        print("Неверный пароль")