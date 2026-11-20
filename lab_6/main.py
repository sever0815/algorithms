from collections import deque


# ---------- Бинарное дерево как структура данных ----------
class Node:
    def __init__(self, val):
        self.val = val       # значение узла
        self.left = None     # левый потомок
        self.right = None    # правый потомок


def build_tree(values):
    """Строит дерево из списка по уровням (None - нет узла), как в условии."""
    if not values:                # пустой список - пустое дерево
        return None
    root = Node(values[0])      # первый элемент - корень
    queue = deque([root])    # узлы, которым ещё нужно раздать потомков
    i = 1                      # следующий элемент списка
    while queue and i < len(values):    # есть кому раздавать и есть что раздавать
        node = queue.popleft()        # берём первого из очереди
        # левый потомок
        if i < len(values) and values[i] is not None:
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1

        # правый потомок
        if i < len(values) and values[i] is not None:
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
    return root


# ---------- Задача A: симметричное дерево ----------
def is_mirror(a, b):
    if a is None and b is None:      # обе ветки закончились - всё совпало
        return True
    if a is None or b is None:       # одна закончилась, другая нет
        return False
    # значения равны, и наружные пары, и внутренние пары тоже зеркальны
    return a.val == b.val and is_mirror(a.left, b.right) and is_mirror(a.right, b.left)


def is_symmetric(root):
    return root is None or is_mirror(root.left, root.right)


# ---------- Задача C: кузены ----------
def find(node, val, parent=None, depth=0):
    """Ищет узел со значением val. Возвращает (родитель, глубина) или None."""
    if node is None:
        return None
    if node.val == val:
        return parent, depth
    return find(node.left, val, node, depth + 1) or find(node.right, val, node, depth + 1)


def is_cousins(root, x, y):
    a = find(root, x)
    b = find(root, y)
    if a is None or b is None:       # одного из узлов нет в дереве
        return False
    # одинаковая глубина и разные родители
    return a[1] == b[1] and a[0] is not b[0]


# ---------- Задача D: поддерево ----------
def same_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)


def is_subtree(root, sub_root):
    if root is None:
        return sub_root is None
    # sub_root совпадает с деревом, начинающимся здесь, или лежит глубже
    return (same_tree(root, sub_root)
            or is_subtree(root.left, sub_root)
            or is_subtree(root.right, sub_root))


# ---------- Примеры из условия ----------
print("A:", is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))              # True
print("A:", is_symmetric(build_tree([1, 2, 2, None, 3, None, 3])))        # False

print("C:", is_cousins(build_tree([1, 2, 3, 4]), 4, 3))                   # False
print("C:", is_cousins(build_tree([1, 2, 3, None, 4, None, 5]), 5, 4))    # True

print("D:", is_subtree(build_tree([3, 4, 5, 1, 2]),
                       build_tree([4, 1, 2])))                            # True
print("D:", is_subtree(build_tree([3, 4, 5, 1, 2, None, None, None, None, 0]),
                       build_tree([4, 1, 2])))                            # False
