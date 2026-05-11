age = int(input())
is_citizen = input() == "True"
disqualification = input() == "True"

if age <= 18 and is_citizen and not disqualification:
    print("Соответствует всем условиям.")
else:
    print("Не соответствует условиям")