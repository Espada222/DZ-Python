import string

text = input("Введите текст: ").lower()
words = text.translate(str.maketrans('', '', string.punctuation)).split()
if not words:
    print("\nТекст не содержит слов.")
else:
    vowels_count = sum(1 for word in words for char in word if char in 'аеёиоуыэюя')
    longest_word = max(words, key=len)
    frequency = {word: words.count(word) for word in set(words)}
    print(f"\nКоличество слов: {len(words)}")
    print(f"Самое длинное слово: '{longest_word}' (длина букв: {len(longest_word)})")
    print(f"Количество гласных букв: {vowels_count}")
    print("\nЧастота встречаемости слов:")
    for w in sorted(frequency):
        print(f"'{w}': {frequency[w]}")
