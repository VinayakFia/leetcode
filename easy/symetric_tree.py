from typing import Optional


class TreeNode:
    val: int
    left: "TreeNode"
    right: "TreeNode"
    
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def util(l, r):
            if l is None and r is None: return True
            if l is None and r is not None: return False
            if l is not None and r is None: return False
            if l.val != r.val: return False
            return util(l.right, r.left) and util(l.left, r.right)
        return util(root, root) 