from collections import deque

graph = {
    "Спасская": ["Достоевская", "Сенная площадь"],
    "Достоевская": ["Спасская", "Владимирская"],
    "Владимирская": ["Достоевская", "Пушкинская", "Площадь Восстания"],
    "Пушкинская": ["Владимирская", "Звенигородская", "Технологический институт"],
    "Звенигородская": ["Пушкинская", "Обводный канал"],
    "Обводный канал": ["Звенигородская"],

    "Садовая": ["Сенная площадь", "Адмиралтейская"],
    "Сенная площадь": ["Садовая", "Спасская", "Технологический институт"],
    "Адмиралтейская": ["Садовая"],

    "Гостиный двор": ["Невский проспект", "Маяковская"],
    "Маяковская": ["Гостиный двор", "Площадь Александра Невского", "Площадь Восстания"],
    "Площадь Александра Невского": ["Маяковская", "Новочеркасская"],
    "Новочеркасская": ["Площадь Александра Невского", "Ладожская"],
    "Ладожская": ["Новочеркасская", "Проспект Большевиков"],
    "Проспект Большевиков": ["Ладожская"],

    "Площадь Восстания": ["Маяковская", "Владимирская"],
    "Технологический институт": ["Пушкинская", "Сенная площадь"],
    "Невский проспект": ["Гостиный двор"],
}


def bfs(start, end):
    if start not in graph or end not in graph:
        return None

    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == end:
            return path

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


def dfs(start, end):
    if start not in graph or end not in graph:
        return None

    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        current = path[-1]

        if current == end:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None


if __name__ == "__main__":
    print("Доступные станции:")
    for station in sorted(graph.keys()):
        print(f"  - {station}")
    print()

    start = input("Начальная станция: ").strip()
    end = input("Конечная станция: ").strip()

    if start not in graph:
        print(f"Станция '{start}' не найдена")
    elif end not in graph:
        print(f"Станция '{end}' не найдена")
    elif start == end:
        print(f"Начало и конец совпадают: {start}")
    else:
        print(f"\nМаршрут: {start} => {end}\n")

        path_bfs = bfs(start, end)
        print("BFS:", " => ".join(path_bfs) if path_bfs else "Путь не найден")

        path_dfs = dfs(start, end)
        print("DFS:", " => ".join(path_dfs) if path_dfs else "Путь не найден")
