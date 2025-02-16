from typing import Optional
from LeetCode import TreeNode
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode], level: int) -> None:
            if left is None:
                return
            if left.left:
                dfs(left.left, right.right, level + 1)
                dfs(right.left, left.right, level + 1)
            if level % 2 == 1:
                left.val, right.val = right.val, left.val
        dfs(root.left, root.right, 1)
        return root