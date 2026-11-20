# Время в минутах
GREEN, PURPLE, BLUE, RED, YELLOW, TRANSFER = 4, 5, 6, 3, 2, 1
INF = float("inf")

# Рёбра: (станция 1, станция 2, минуты)
edges = [
    ("Спасская", "Достоевская", YELLOW),
    ("Достоевская", "Лиговский проспект", YELLOW),
    ("Лиговский проспект", "Площадь Александра Невского", YELLOW),
    ("Площадь Александра Невского", "Новочеркасская", YELLOW),
    ("Новочеркасская", "Ладожская", YELLOW),
    ("Ладожская", "Проспект Большевиков", YELLOW),
    ("Площадь Восстания", "Владимирская", RED),
    ("Владимирская", "Пушкинская", RED),
    ("Пушкинская", "Технологический институт", RED),
    ("Невский проспект", "Сенная площадь", BLUE),
    ("Сенная площадь", "Технологический институт", BLUE),
    ("Гостиный двор", "Маяковская", GREEN),
    ("Маяковская", "Площадь Александра Невского", GREEN),
    ("Адмиралтейская", "Садовая", PURPLE),
    ("Садовая", "Звенигородская", PURPLE),
    ("Звенигородская", "Обводный канал", PURPLE),
    # переходы
    ("Невский проспект", "Гостиный двор", TRANSFER),
    ("Площадь Восстания", "Маяковская", TRANSFER),
    ("Достоевская", "Владимирская", TRANSFER),
    ("Пушкинская", "Звенигородская", TRANSFER),
    ("Сенная площадь", "Спасская", TRANSFER),
    ("Сенная площадь", "Садовая", TRANSFER),
    ("Спасская", "Садовая", TRANSFER),
]

# Граф: станция -> {сосед: минуты}. Метро ходит в обе стороны, поэтому добавляем оба направления.
# Из списка рёбер собираем словарь "станция -> {сосед: минуты}"
graph = {}
for a, b, w in edges:
    graph.setdefault(a, {})[b] = w
    graph.setdefault(b, {})[a] = w


def dijkstra(start, end):
    time = {s: INF for s in graph}   # лучшее найденное время до каждой станции
    prev = {}                        # откуда пришли на станцию (для восстановления пути)
    time[start] = 0
    unvisited = set(graph)          # станции, которые ещё не обработаны.

    while unvisited:
        # 1. берём непосещённую станцию с наименьшим временем
        current = min(unvisited, key=lambda s: time[s])
        if time[current] == INF:     # до остальных не добраться
            break
        unvisited.remove(current)

        # 2. пробуем улучшить время до её соседей
        for neighbor, w in graph[current].items():
            if time[current] + w < time[neighbor]:
                time[neighbor] = time[current] + w
                prev[neighbor] = current

    if time[end] == INF:
        return None, INF

    # 3. восстанавливаем путь: идём от конца к началу по prev
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    return path[::-1], time[end]


# ---------- Ввод / вывод ----------
print("Станции метро:")
for station in sorted(graph):
    print(" ", station)
print()

line = input("Вход (например: Спасская, Пушкинская): ")
start, end = [s.strip() for s in line.split(",")]

if start not in graph or end not in graph:
    print("Станция не найдена")
else:
    path, total = dijkstra(start, end)
    if path is None:
        print("Путь не найден")
    else:
        print("->".join(path) + ", " + str(total) + " минут")
