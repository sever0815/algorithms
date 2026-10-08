import random
import time
import sys

# Увеличиваем лимит рекурсии для работы Quick Sort с большими массивами
sys.setrecursionlimit(2000000)

# 1. Генерация данных
def generate_products(count):
    nazvania = ["Кабель", "Мышь", "Монитор", "Ноутбук", "Принтер", "Наушники", 
                "Клавиатура", "Флешка", "Видеокарта", "Жесткий диск", "Камера", 
                "Фотоаппарат", "Видеокамера", "Смартфон", "Аэрогриль", 
                "Соковыжималка", "Пылесос", "Тостер", "Микроволновка"]

    product_list = []
    # Генерируем уникальные ID (не отсортированные)
    ids = random.sample(range(1, 2000000), count)

    for i in range(count):
        product = {
            "id": ids[i],
            "name": random.choice(nazvania)
        }
        product_list.append(product)
    return product_list

# 2. Алгоритмы сортировки

# Пузырьковая сортировка
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j]['id'] > arr[j + 1]['id']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j]['id'] > key_item['id']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# Быстрая сортировка
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]['id']
    left = [x for x in arr if x['id'] < pivot]
    middle = [x for x in arr if x['id'] == pivot]
    right = [x for x in arr if x['id'] > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 3. Тестирование и замеры
def run_test():
    TOTAL_ITEMS = 1000000
    TEST_SMALL = 5000 

    print(f"--- Генерация {TOTAL_ITEMS} товаров ---")
    full_list = generate_products(TOTAL_ITEMS)
    print("Генерация завершена.\n")

    results = {}

    # Тест Quick Sort на полном списке
    print(f"--- Тест Quick Sort ({TOTAL_ITEMS} элементов) ---")
    start = time.perf_counter()
    quick_sort(full_list.copy())
    results["Quick Sort"] = time.perf_counter() - start
    print(f"Время выполнения: {results['Quick Sort']:.4f} сек.\n")

    # Тест простых сортировок на малом списке
    small_list = full_list[:TEST_SMALL]
    print(f"--- Тест простых сортировок ({TEST_SMALL} элементов) ---")

    start = time.perf_counter()
    bubble_sort(small_list.copy())
    results["Bubble Sort"] = time.perf_counter() - start
    print(f"Bubble Sort: {results['Bubble Sort']:.4f} сек.")

    start = time.perf_counter()
    insertion_sort(small_list.copy())
    results["Insertion Sort"] = time.perf_counter() - start
    print(f"Insertion Sort: {results['Insertion Sort']:.4f} сек.")

    # Таблица результатов
    print("\n" + "=" * 60)
    print("ТАБЛИЦА РЕЗУЛЬТАТОВ")
    print("=" * 60)
    print(f"{'Алгоритм':<20} | {'Размер данных':<15} | {'Время (сек)':<12}")
    print("-" * 60)
    print(f"{'Quick Sort':<20} | {TOTAL_ITEMS:<15} | {results['Quick Sort']:<12.4f}")
    print(f"{'Bubble Sort':<20} | {TEST_SMALL:<15} | {results['Bubble Sort']:<12.4f}")
    print(f"{'Insertion Sort':<20} | {TEST_SMALL:<15} | {results['Insertion Sort']:<12.4f}")
    print("=" * 60)

    # Выводы
    print("\nВЫВОДЫ:")
    print("1. Пузырьковая и сортировка вставками имеют сложность O(n²) и эффективны только для малых массивов.")
    print("2. Быстрая сортировка (Quick Sort) имеет среднюю сложность O(n log n) и значительно быстрее на больших данных.")
    print("3. Для сортировки 1 000 000 элементов Quick Sort — оптимальный выбор.")
    print("4. Простые сортировки могут быть полезны для почти отсортированных данных или малых списков.")

if __name__ == "__main__":
    run_test()
