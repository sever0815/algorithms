import time
import random

# 1. Генерация данных
def generate_products(n=1_000_000):
    products = []
    # Генерируем уникальные ID, уже отсортированные
    ids = sorted(random.sample(range(1, n * 10), n))
    for i in range(n):
        products.append({"id": ids[i], "name": f"Product {ids[i]}"})
    return products

# Алгоритмы поиска
def linear_search(products, target_id):
    # Линейный поиск
    for product in products:
        if product["id"] == target_id:
            return product
    return None

def binary_search(products, target_id):
    # Бинарный поиск
    low = 0
    high = len(products) - 1
    while low <= high:
        mid = (low + high) // 2
        if products[mid]["id"] == target_id:
            return products[mid]
        elif products[mid]["id"] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def exponential_search(products, target_id):
    # Экспоненциальный поиск
    if products[0]["id"] == target_id:
        return products[0]
    
    n = len(products)
    i = 1
    while i < n and products[i]["id"] <= target_id:
        i *= 2
    
    # Бинарный поиск в диапазоне [i/2, min(i, n-1)]
    left = i // 2
    right = min(i, n - 1)
    
    # Реализация простого бинарного поиска для диапазона
    low = left
    high = right
    while low <= high:
        mid = (low + high) // 2
        if products[mid]["id"] == target_id:
            return products[mid]
        elif products[mid]["id"] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def interpolation_search(products, target_id):
    # Интерполяционный поиск
    low = 0
    high = len(products) - 1
    
    while low <= high and products[low]["id"] <= target_id <= products[high]["id"]:
        if products[low]["id"] == products[high]["id"]:
            if products[low]["id"] == target_id:
                return products[low]
            else:
                return None
        
        # Формула: pos = low + [(target - arr[low]) * (high - low) / (arr[high] - arr[low])]
        pos = low + ((target_id - products[low]["id"]) * (high - low) // (products[high]["id"] - products[low]["id"]))
        
        if products[pos]["id"] == target_id:
            return products[pos]
        elif products[pos]["id"] < target_id:
            low = pos + 1
        else:
            high = pos - 1
            
    return None

# Выполнение и замеры
def run_tests():
    products = generate_products()
    
    test_ids = [
        products[0]["id"],                # Начало
        products[len(products)//2]["id"], # Середина
        products[-1]["id"],               # Конец
        products[random.randint(0, len(products)-1)]["id"], # Случайный
        -1                                # Отсутствует
    ]
    
    algorithms = {
        "Linear": linear_search,
        "Binary": binary_search,
        "Exponential": exponential_search,
        "Interpolation": interpolation_search
    }
    
    results = []
    
    # Замер времени для каждого алгоритма
    for algo_name, algo_func in algorithms.items():
        for target in test_ids:
            start_time = time.perf_counter()
            algo_func(products, target)
            end_time = time.perf_counter()
            results.append((algo_name, target, end_time - start_time))
            
    # Вывод таблицы результатов
    print("\n" + "=" * 83)
    header = f"{'Алгоритм':<13} | {'В начале':<11} | {'В середине':<11} | {'В конце':<11} | {'Случайный':<11} | {'Отсутствует'}"
    print(header)
    
    # Названия для отображения
    display_names = {
        "Linear": "Линейный",
        "Binary": "Бинарный",
        "Exponential": "Экспоненц-й",
        "Interpolation": "Интерполяц-й"
    }
    for algo_name in algorithms.keys():
        row = f"{display_names[algo_name]:<13} |"
        for i in range(len(test_ids)):
            # Поиск времени для алгоритма и теста
            time_val = next(r[2] for r in results if r[0] == algo_name and r[1] == test_ids[i])
            row += f" {time_val:<8.6f}s   |"
        print(row[:-2]) # Удалить последний разделитель
    print("=" * 83)

    print("\nВыводы:")
    print("1. Линейный поиск самый медленный для больших наборов данных (O(n)).")
    print("2. Бинарный, Экспоненциальный и Интерполяционный поиски значительно быстрее (O(log n) или лучше).")
    print("3. Интерполяционный поиск может быть самым быстрым на равномерно распределенных данных.")
    print("4. Экспоненциальный поиск эффективен для больших отсортированных массивов.")

if __name__ == "__main__":
    run_tests()
