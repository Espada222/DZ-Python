def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


def empty_function():
    pass


def test_max_number():
    assert max_number(10, 5) == 10, "Ошибка: max_number(10, 5) должно быть 10"

    assert max_number(3, 7) == 7, "Ошибка: max_number(3, 7) должно быть 7"

    assert max_number(4, 4) == 4, "Ошибка: max_number(4, 4) должно быть 4"

    assert max_number(-1, -5) == -1, "Ошибка: max_number(-1, -5) должно быть -1"

    print("Все тесты функции max_number пройдены успешно!")


if __name__ == "__main__":

    test_max_number()

    result1 = max_number(2, 1)
    result2 = max_number(1, 3)
    print(f"Результат 1: {result1}")
    print(f"Результат 2: {result2}")

    empty_function()

    n = 10
    print(f"Четные числа до {n}:")
    for num in even_numbers(n):
        print(num)