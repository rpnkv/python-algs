import math
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, __value):
        from algs.fundamental.trees.tree_ops import are_equal
        return are_equal(self, __value)

    @staticmethod
    def from_level_order_array(array_repr: list[int]):  # TODO add return value
        """
        1. The main idea.
        The algorithm is built upon the 'depth counter' variable. At each iteration, we check, if array length is big
        enough to fit next tree's nodes level. If it does -- run the main loop, attaching next level's values to a
        previous ones.

        2. Non-fitting input cases breakthrough
        - empty array -> return None;
        - input array of len 1 -> return TreeNode(array_repr[0])

        3. Main execution path breakthrough
        3.1 Global (outside cycle) variables:
            1. current_parents

        3.2 Main loop
            Словесное описание: если длинна массива позволяет вместить дочерние узлы для текущего количества
            родительских -- выполняем цикл. Количество узлов в дереве определяется по формуле: math.pow(2, depth) - 1.
            Проверяем:
             - глубина 1: 2pow1 - 1 = 1;
             - глубина 2: 2pow2 - 1 = 3;
             - глубина 3: 2pow3 - 7 = 7.

        3.3 Внутренний цикл итерации детей
            Задача: определить начальный и конечный индексы.
            Решение: опираясь на длинну родительского массива, можно определить, на каком индексе "он бы закончился",
            используя формулу из пункта выше. Назовём её left_pointer и будем вычислять в начале каждого цикла.

            Range можно определить по длинне родительского массива, в каждой итерации внутреннего цикла обращаясь к
            left_pointer + i*2 для левого потомка, и left_pointer + i*2 + 1 для правого.



        Using 'depth counter' value, we calculate the shift within array, we start looking for 'child nodes' from.
        Then, iterating over 'parent nodes', we're looking for appropriate child node, and, if it exists, append it to
        a parent node.
        Current child nodes collection must be saved and then set as current 'parent nodes' for next loop.

        Approximate corner cases:


        Main loop condition examples:
        - for list with depth 1, expected arr len is 1;
        - for list wuth depth 2, expected arr len us 3;
        - for list with depth 3, expected arr len is 1 + 3 + 4 => 7;

        So it's 'while len(array_repr) > math.pow(2, depth) - 1'

        Depth initial value considerations.
        We check if the algo state is valid for the next loop, before we actually proceed it. So, before loop has
        started, we must check if array is long enough before proceed.
        So, as we process 'depth 1' before entering the loop, I consider initial value to 2.
        Then we check if the array is long enough to supply this level values.
        After processing is over, depth level is increased.
        """

        if len(array_repr) == 0:
            return None

        root = TreeNode(array_repr[0])
        if len(array_repr) == 1:
            return root

        parents = [root]
        left_pointer = 1
        while left_pointer < len(array_repr):
            children = []

            for parent_index in range(0, len(parents)):
                # left child
                left_value_index = left_pointer + parent_index * 2
                left_value = array_repr[left_value_index]
                if left_value is not None:
                    left_leaf = TreeNode(left_value)
                    parents[parent_index].left = left_leaf
                    children.append(left_leaf)
                else:
                    children.append(None)

                right_value_index = left_pointer + parent_index * 2 + 1
                right_value = array_repr[right_value_index]
                if right_value is not None:
                    right_leaf = TreeNode(right_value)
                    parents[parent_index].right = right_leaf
                    children.append(right_leaf)
                else:
                    children.append(None)

            parents = children
            left_pointer = int(math.pow(2, len(parents))) - 1

        return root

    @staticmethod
    def from_leetcode_array(arr: list[Optional[int]]) -> Optional[TreeNode]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1
        n = len(arr)

        while queue and i < n:
            node = queue.popleft()

            if i < n and arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)
            i += 1

            if i < n and arr[i] is not None:
                node.right = TreeNode(arr[i])
                queue.append(node.right)
            i += 1

        return root

    def _to_level_order_as_arrays(self) -> list[list[int]]:
        """
            Iterating the tree level-by level.

            Loop algorithm.
            Variables:
                condition: while any of processing nodes isn't a null.
                input:
                    - processing nodes list, start with root node.
                expected product:
                    - current nodes siblings, appended as nodes to the intermediate list and values to output.
                state switch:
                    - siblings become root nodes before switching to new iteration.

       """
        out = []
        current_parent_nodes = [self]

        while any(map(lambda node: node is not None, current_parent_nodes)):
            current_children = []

            for parent in current_parent_nodes:
                if parent is not None:
                    current_children += [parent.left, parent.right]
                else:
                    current_children += [None, None]

            out.append([*map(lambda node: node.val if node is not None else None, current_parent_nodes)])
            current_parent_nodes = current_children

        return out

    def to_level_order_array(self) -> list[int]:
        """
        Performs flattening of _to_level_order_as_arrays.
        """
        level_order_arrays = self._to_level_order_as_arrays()

        out = []

        for array in level_order_arrays:
            out += array

        return out

    def to_string_tree(self) -> str:
        level_order_arrays = self._to_level_order_as_arrays()

        max_len = len(level_order_arrays[-1]) - 1

        out = []

        for array in level_order_arrays:
            out.append(" ".join([*map(lambda x: str(x), array)]))

        return "\n".join(out)
