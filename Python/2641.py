from typing import Optional
from ..TreeNode import TreeNode, generate_TreeNode, generate_List
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        Sum = []
        def DFS1(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            if level == len(Sum):
                Sum.append(0)
            Sum[level] += root.val
            DFS1(root.left, level + 1)
            DFS1(root.right, level + 1)
        def DFS2(root: Optional[TreeNode], level: int) -> None:
            if level >= len(Sum):
                return
            left, right = 0, 0
            if root.left:
                left = root.left.val
            if root.right:
                right = root.right.val
            if root.left:
                root.left.val = Sum[level] - left - right
                DFS2(root.left, level + 1)
            if root.right:
                root.right.val = Sum[level] - left - right
                DFS2(root.right, level + 1)
        DFS1(root, 0)
        if root:
            root.val = 0
            DFS2(root, 1)
        return root