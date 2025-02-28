from typing import Optional
from ..TreeNode import TreeNode, generate_TreeNode, generate_List
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.recover = set()
        def dfs(node: Optional[TreeNode], val: int):
            if not node:
                return
            node.val = val
            self.recover.add(val)
            dfs(node.left, 2 * val + 1)
            dfs(node.right, 2 * val + 2)
        if root:
            dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.recover