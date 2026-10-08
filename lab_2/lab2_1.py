import random
from ipaddress import IPv4Address
from typing import Any
from collections import Counter

# Определение типа для логов
Log = dict[str, Any]

# 1. Поразрядная сортировка (Radix Sort) для IP-адресов
def radix_sort_ipv4(logs: list[Log]) -> list[Log]:
    # Преобразуем IP-адреса в целые числа для удобства сортировки
    items = [(int(IPv4Address(log["ip"])), log) for log in logs]
    # Сортируем по каждому байту (4 байта в IPv4)
    for shift in (0, 8, 16, 24):
        buckets: list[list[tuple[int, Log]]] = [[] for _ in range(256)]
        for ip_number, log in items:
            byte = (ip_number >> shift) & 0xFF
            buckets[byte].append((ip_number, log))
        items = [item for bucket in buckets for item in bucket]
    return [log for _, log in items]

# 2. Сортировка подсчетом (Counting Sort) по HTTP-статусам
def counting_sort_status(logs: list[Log]) -> dict[int, list[Log]]:
    # Создаем корзины для статусов от 100 до 599
    buckets: dict[int, list[Log]] = {status: [] for status in range(100, 600)}
    for log in logs:
        status = log["status"]
        buckets[status].append(log)
    return buckets


# Финальная сортировка: сначала по IP, затем по статусу
def final_sort(logs: list[Log]) -> dict[int, list[Log]]:
    logs_by_ip = radix_sort_ipv4(logs)
    return counting_sort_status(logs_by_ip)


# Генерация тестовых логов
def gener(n: int = 8_000, seed: int = 55) -> list[Log]:
    rng = random.Random(seed)
    logs: list[Log] = []
    # Генерируем случайные логи
    for _ in range(n):
        ip = str(IPv4Address(rng.getrandbits(32)))
        status = rng.randint(100, 599)
        logs.append({
            "ip": ip,
            "status": status,
        })
    # Генерируем "атакующие" IP
    base_ip = rng.getrandbits(32)
    for _ in range(2_000):
        ip = str(IPv4Address(base_ip + rng.randint(0, 50)))
        status = rng.randint(100, 599)
        logs.append({
            "ip": ip,
            "status": status,
        })

    return logs


def run_test():
    logs = gener(8_000)
    
    # 1. Сортировка по IP
    by_ip = radix_sort_ipv4(logs)
    print(f"Всего записей: {len(by_ip)}")
    print("=" * 60)
    print("1. СОРТИРОВКА ТОЛЬКО ПО IP (Radix Sort)")
    print("=" * 60)
    print("\nПервые 10 записей (по возрастанию IP):")
    for log in by_ip[:10]:
        print(f"  {log['ip']:>16}  status={log['status']}")

    print("\nПоследние 10 записей:")
    for log in by_ip[-10:]:
        print(f"  {log['ip']:>16}  status={log['status']}")
        
    # 2. Сортировка по статусу
    by_status = counting_sort_status(logs)
    non_empty = {s: b for s, b in by_status.items() if b}

    print("\n" + "=" * 60)
    print("2. СОРТИРОВКА ТОЛЬКО ПО СТАТУСУ (Counting Sort)")
    print("=" * 60)
    print(f"Уникальных статусов: {len(non_empty)}")

    print("\nПервые 10 статусов (по возрастанию кода):")
    for status in sorted(non_empty)[:10]:
        print(f"  {status}: {len(non_empty[status]):>4} записей")

    print("\nПоследние 10 статусов:")
    for status in sorted(non_empty)[-10:]:
        print(f"  {status}: {len(non_empty[status]):>4} записей")
        
    # 3. Финальная сортировка
    report = final_sort(logs)
    report_non_empty = {s: b for s, b in report.items() if b}

    print("\n" + "=" * 60)
    print("3. ФИНАЛЬНАЯ СОРТИРОВКА (IP внутри статусов)")
    print("=" * 60)
    print(f"Уникальных статусов: {len(report_non_empty)}")
    print("\nПервые 5 статуса с записями (IP упорядочены):")
    for status in sorted(report_non_empty)[:5]:
        bucket = report_non_empty[status]
        print(f"\n  --- {status} --- ({len(bucket)} записей)")
        for log in bucket[:3]:
            print(f"    {log['ip']:>16}  status={log['status']}")

    # 4. Анализ DDoS
    print("\n" + "=" * 60)
    print("4. DDoS-АНАЛИЗ")
    print("=" * 60)
    all_ips = Counter(log["ip"] for log in logs)
    print("\nТоп-10 IP по общему количеству запросов:")
    for ip, cnt in all_ips.most_common(10):
        print(f"  {ip:>16}  {cnt}")

    print("\nТоп-5 IP в каждом из ключевых статусов (200 / 404 / 500):")
    for status in (200, 404, 500):
        bucket = report.get(status, [])
        top = Counter(log["ip"] for log in bucket).most_common(5)
        print(f"\n  --- {status} --- ({len(bucket)} записей)")
        for ip, cnt in top:
            print(f"    {ip:>16}  {cnt}")


if __name__ == "__main__":
    run_test()
