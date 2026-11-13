GREEN = 4
PURPLE = 5
BLUE = 6
RED = 3
YELLOW = 2
TRANSFER = 1

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
    ("Невский проспект", "Гостиный двор", TRANSFER),
    ("Площадь Восстания", "Маяковская", TRANSFER),
    ("Достоевская", "Владимирская", TRANSFER),
    ("Пушкинская", "Звенигородская", TRANSFER),
    ("Сенная площадь", "Спасская", TRANSFER),
    ("Сенная площадь", "Садовая", TRANSFER),
    ("Спасская", "Садовая", TRANSFER),
]


def shortest_path(start, end):
    dist = {start: 0}  # минуты до станции
    prev = {}  # откуда пришли (для восстановления маршрута)
    queue = [start]  # станции, до которых дошли, но соседей еще не раскрыли

    while queue:
        cur = min(queue, key=lambda s: dist[s])
        queue.remove(cur)

        for a, b, w in edges:
            if a == cur:
                nxt = b
            elif b == cur:
                nxt = a
            else:
                continue

            new_time = dist[cur] + w
            if nxt not in dist or new_time < dist[nxt]:
                dist[nxt] = new_time
                prev[nxt] = cur
                queue.append(nxt)

    if end not in dist:
        return None, None

    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()

    return path, dist[end]

print("Станции метро:")
for station in sorted({s for a, b, _ in edges for s in (a, b)}):
    print("  ", station)
print("\nДля выхода введите 'выход'\n")

while True:
    start = input("Начальная станция: ").strip()
    if start == "выход":
        break
    end = input("Конечная станция: ").strip()

    path, total = shortest_path(start, end)
    if path is None:
        print("Станция не найдена или пути нет\n")
    else:
        print(" -> ".join(path), "-", total, "минут\n")
