from typing import Optional

from common.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        from collections import deque
        d = deque()
        d.append(root)

        depth = 0

        while d:
            depth += 1
            for _ in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)

                if node.right:
                    d.append(node.right)

        return depth
