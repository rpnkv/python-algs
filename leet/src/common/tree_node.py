import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, __value):
        current_level_equals = self.val == __value.val

        left_equals = (self.left is None and __value.left is None
                       ) or (
                              self.left is not None and __value.left is not None and self.left == __value.left)

        right_equals = (
                               self.right is None and __value.right is None
                       ) or (self.right is not None and __value.right is not None and self.right == __value.right)
        return current_level_equals and left_equals and right_equals

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

        if len(array_repr) == 1:
            return TreeNode(array_repr[0])

        processing_depth = 2
        current_depth_starting_index=1
        while len(array_repr) > int(math.pow(2, processing_depth)):


            processing_depth += 1

        return TreeNode()





