age = int(input())
is_citizen = input() == "True"
disqualification = input() == "True"

if age < 18:
    print(False)
    print("Причина: Слишком молод(а).")
elif not is_citizen:
    print(False)
    print("Причина: Не гражданин (гражданка).")
elif disqualification:
    print(False)
    print("Причина: Дисквалифицирован(а), есть уголовное наказание.")
else:
    print(True)
    print("Причина: Соответствует всем условиям.")