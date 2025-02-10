from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def generate_TreeNode(List: list) -> Optional[TreeNode]:
    if not List:
        return None
    root = TreeNode(List[0])
    queue = [root]
    i = 1

    while i < len(List):
        node = queue.pop(0)
        
        if List[i] is not None:
            node.left = TreeNode(List[i])
            queue.append(node.left)
        i += 1
        
        if i < len(List) and List[i] is not None:
            node.right = TreeNode(List[i])
            queue.append(node.right)
        i += 1

    return root

def generate_List(root: Optional[TreeNode]) -> list:
    result = []
    if not root:
        return result
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
