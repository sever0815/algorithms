from collections import deque
from typing import Optional


class TreeNode:
    """Узел бинарного дерева."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Строит бинарное дерево из списка в порядке level-order (по уровням).
    None означает отсутствие узла.
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Левый потомок
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Правый потомок
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


# Задача A: Проверка симметричности дерева
def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    Проверяет, является ли дерево зеркальным отражением самого себя.
    """
    if root is None:
        return True

    def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    return is_mirror(root.left, root.right)


# Задача B: Диаметр дерева
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Возвращает длину диаметра дерева (наибольший путь между двумя узлами).
    """
    diameter = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Обновляем диаметр
        diameter = max(diameter, left_height + right_height)

        return max(left_height, right_height) + 1

    height(root)
    return diameter


# Задача D: Проверка поддерева
def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    """
    Проверяет, является ли sub_root поддеревом root.
    """
    if sub_root is None:
        return True
    if root is None:
        return False

    if is_same_tree(root, sub_root):
        return True

    return is_subtree(root.left, sub_root) or is_subtree(root.right, sub_root)


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """Проверяет, идентичны ли два дерева."""
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    return (p.val == q.val and
            is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))


# Тестирование
def run_tests():
    print("=" * 70)
    print("Лабораторная работа 6. Деревья")
    print("=" * 70)

    # Задача A: Симметричность
    print("\n" + "=" * 70)
    print("ЗАДАЧА A: Проверка симметричности дерева")
    print("=" * 70)

    # Пример 1: [1,2,2,3,4,4,3] -> true
    tree_a1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    result_a1 = is_symmetric(tree_a1)
    print(f"\nВход: [1,2,2,3,4,4,3]")
    print(f"Выход: {result_a1} (ожидалось: true)")

    # Пример 2: [1,2,2,null,3,null,3] -> false
    tree_a2 = build_tree([1, 2, 2, None, 3, None, 3])
    result_a2 = is_symmetric(tree_a2)
    print(f"\nВход: [1,2,2,null,3,null,3]")
    print(f"Выход: {result_a2} (ожидалось: false)")

    # Задача B: Диаметр
    print("\n" + "=" * 70)
    print("ЗАДАЧА B: Диаметр дерева")
    print("=" * 70)

    # Пример 1: [1,2,3,4,5] -> 3
    tree_b1 = build_tree([1, 2, 3, 4, 5])
    result_b1 = diameter_of_binary_tree(tree_b1)
    print(f"\nВход: [1,2,3,4,5]")
    print(f"Выход: {result_b1} (ожидалось: 3)")

    # Пример 2: [1,2] -> 1
    tree_b2 = build_tree([1, 2])
    result_b2 = diameter_of_binary_tree(tree_b2)
    print(f"\nВход: [1,2]")
    print(f"Выход: {result_b2} (ожидалось: 1)")

    # Задача D: Поддерево
    print("\n" + "=" * 70)
    print("ЗАДАЧА D: Проверка поддерева")
    print("=" * 70)

    # Пример 1: root = [3,4,5,1,2], subRoot = [4,1,2] -> true
    root_d1 = build_tree([3, 4, 5, 1, 2])
    sub_d1 = build_tree([4, 1, 2])
    result_d1 = is_subtree(root_d1, sub_d1)
    print(f"\nВход: root = [3,4,5,1,2], subRoot = [4,1,2]")
    print(f"Выход: {result_d1} (ожидалось: true)")

    # Пример 2: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2] -> false
    root_d2 = build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
    sub_d2 = build_tree([4, 1, 2])
    result_d2 = is_subtree(root_d2, sub_d2)
    print(f"\nВход: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]")
    print(f"Выход: {result_d2} (ожидалось: false)")


if __name__ == "__main__":
    run_tests()
