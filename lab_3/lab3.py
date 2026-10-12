# Лабораторная работа 3. Хэш-таблицы

# ============================================================
# Задача A: Проверка подмножества
# ============================================================
def is_subset(arr1, arr2):
    """
    Проверяет, является ли arr2 подмножеством arr1.
    Использует хэш-таблицу (set) для проверки вхождения.
    """
    set1 = set(arr1)
    for item in arr2:
        if item not in set1:
            return False
    return True


# ============================================================
# Задача B: Первый неповторяющийся символ
# ============================================================
def first_unique_char(s):
    """
    Возвращает первый неповторяющийся символ в строке.
    Использует хэш-таблицу (dict) для подсчёта вхождений.
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in s:
        if char_count[char] == 1:
            return char
    return None


# ============================================================
# Задача C: Длина самого длинного палиндрома
# ============================================================
def longest_palindrome(s):
    """
    Возвращает длину самого длинного палиндрома,
    который можно построить из букв строки s.
    Использует хэш-таблицу (dict) для подсчёта символов.
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    length = 0
    odd_found = False

    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    if odd_found:
        length += 1

    return length


# ============================================================
# Задача D: Проверка анаграмм
# ============================================================
def is_anagram(s, t):
    """
    Проверяет, является ли t анаграммой s.
    Использует хэш-таблицу (dict) для подсчёта символов.
    """
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for char in t:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True


# ============================================================
# Тестирование
# ============================================================
def run_tests():
    print("=" * 60)
    print("ЗАДАЧА A: Проверка подмножества")
    print("=" * 60)

    test_cases_a = [
        (["a", "b", "c", "d", "e", "f"], ["b", "d", "f"], True),
        (["a", "b", "c", "d", "e", "f"], ["b", "d", "f", "h"], False),
    ]

    for arr1, arr2, expected in test_cases_a:
        result = is_subset(arr1, arr2)
        status = "✓" if result == expected else "✗"
        print(f"{status} {arr2} подмножество {arr1}: {result} (ожидалось {expected})")

    print("\n" + "=" * 60)
    print("ЗАДАЧА B: Первый неповторяющийся символ")
    print("=" * 60)

    test_cases_b = [
        ("minimum", "n"),
        ("aabbcc", None),
        ("abcabc", None),
        ("z", "z"),
    ]

    for s, expected in test_cases_b:
        result = first_unique_char(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Первый уникальный в '{s}': {result} (ожидалось {expected})")

    print("\n" + "=" * 60)
    print("ЗАДАЧА C: Длина самого длинного палиндрома")
    print("=" * 60)

    test_cases_c = [
        ("abccccdd", 7),
        ("a", 1),
        ("aAbBABba", 8),
        ("abcdefghijklmnoPQrstuvwxyz", 1),
        ("wasitacaroracatisaw", 19),
        ("bbbabab", 7),
        ("abcdeedcba", 10),
        ("looooooongestpalindrOme", 13),
        ("abcdeedcbaxyz", 11),
    ]

    for s, expected in test_cases_c:
        result = longest_palindrome(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Длина палиндрома для '{s[:30]}...': {result} (ожидалось {expected})")

    print("\n" + "=" * 60)
    print("ЗАДАЧА D: Проверка анаграмм")
    print("=" * 60)

    test_cases_d = [
        ("анаграмма", "амгармана", True),
        ("анаграмма", "грамм", False),
        ("нора", "рано", True),
        ("монета", "отмена", True),
        ("мышка", "камыш", True),
        ("тормони", "монитор", True),
        ("тоемони", "монитор", False),
    ]

    for s, t, expected in test_cases_d:
        result = is_anagram(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{t}' анаграмма '{s}': {result} (ожидалось {expected})")


if __name__ == "__main__":
    run_tests()
