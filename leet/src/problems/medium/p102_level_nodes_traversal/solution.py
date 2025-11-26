import math
from typing import Optional, List

from common.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Top-level concepts.
        1. We must know which level we are currently at, so we can now, how many "children" does it have.
        2. As the relation is one-directed, we must store current children parents, when processing some level.
        3. Continue the parents->children conversion loop until there are no more children.

        Implementation sketch:
        At each loop, we:
        1. Instantiate an array for all children nodes values.
        2. Traverse over all parents, storing either child or None if there is no node.
        3. Collect children node values to a temporary list.
        4. Repeat until children list is empty.

        Key implementation details:
        1. Which loop do we use for this task?
        "While?".

        2. What's the loop condition?
        "If the parent list is empty"?

        3. Depending on a 'current_depth', the amount of parent nodes must be certain. Let's assume it's equal to
        2 pow 'current_depth'. For each parent node entry, two operations must be performed, collect both left and
        right children. So, external loop will include an internal loop.

        4. If we do have, at least one child, we set up 'repeat condition flag' to 'true'.
        """

        if root is None:
            return []

        current_depth = 0
        global_parents = [root]
        more_nodes_exist = True

        results = [[root.val]]

        while more_nodes_exist:
            current_children_nodes = []

            more_nodes_exist: bool = False

            for parent_index in range(int(math.pow(2, current_depth))):
                current_results = []
                local_parent = global_parents[parent_index]
                if local_parent is not None:
                    left_child = local_parent.left
                    if left_child is not None:
                        current_results.append(left_child.val)
                        more_nodes_exist = True
                    else:
                        current_results.append(None)

                    current_children_nodes.append(left_child)

                    right_child = local_parent.right
                    if right_child is not None:
                        current_results.append(right_child.val)
                        more_nodes_exist = True
                    else:
                        current_results.append(None)
                    current_children_nodes.append(right_child)

                if len(current_results) != 0 and (current_results[0] is not None or current_results[1] is not None):
                    results.append([current_result for current_result in current_results if current_result is not None])

            global_parents = current_children_nodes
            current_depth += 1

        return results
