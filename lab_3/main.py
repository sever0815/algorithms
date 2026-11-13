# A задача:
def is_subset(big: list, small: list) -> bool:
    big_set = set(big)          # хэш-таблица
    return all(x in big_set for x in small)


# Проверка на примерах
print("===A===")
print(is_subset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]))
print(is_subset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f", "h"]))



# B задача:
def first_unique_char(s: str) -> str:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return ""   # если такого нет

print("\n===B===")
print(first_unique_char("minimum"))



# C задача:
def longest_palindrome(s: str) -> int:
    # Хэш-таблица: символ -> количество вхождений
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    length = 0
    has_odd = False

    for cnt in freq.values():
        length += (cnt // 2) * 2       # берём все пары
        if cnt % 2 == 1:
            has_odd = True             # есть символ для центра

    return length + (1 if has_odd else 0)


# Примеры из задания
print("\n===C===")
print(longest_palindrome("abccccdd"))  # 7
print(longest_palindrome("a"))         # 1

# Тест-кейсы
tests = [
    ("aAbBABba", 8),
    ("abcdefghijklmnoPQrstuvwxyz", 1),
    ("wasitacaroracatisaw", 19),
    ("bbbabab", 7),
    ("abcdeedcba", 10),
    ("looooooongestpalindrOme", 13),
    ("abcdeedcbaxyz", 11),
]
for s, expected in tests:
    got = longest_palindrome(s)
    print(f"{s!r:35} -> {got:3}  (ожидалось {expected})  {'OK' if got == expected else 'FAIL'}")

# Самый длинный тест-кейс
big = "abbbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"
print(f"Длинный тест -> {longest_palindrome(big)} (ожидалось 1122)  "
      f"{'OK' if longest_palindrome(big) == 1122 else 'FAIL'}")



# D задача:
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    # Хэш-таблица: символ -> количество вхождений в s
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Уменьшаем счётчики по символам t
    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True


# Примеры
print("\n===D===")
print(is_anagram("анаграмма", "амгармана"))  # True
print(is_anagram("анаграмма", "грамм"))      # False

# Тест-кейсы
tests = [
    ("нора", "рано", True),
    ("монета", "отмена", True),
    ("мышка", "камыш", True),
    ("тормони", "монитор", True),
    ("тоемони", "монитор", False),
]
for s, t, expected in tests:
    got = is_anagram(s, t)
    print(f"{s!r:12} / {t!r:12} -> {got}  (ожидалось {expected})  {'OK' if got == expected else 'FAIL'}")
