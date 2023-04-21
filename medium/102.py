


#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res: list[list[int]] = []
        
        def util(node: TreeNode, level: int) -> None:
            nonlocal res
            if len(res) < level + 1:
                res.append([])
            if node is None:
                res[level].append(None)
            else:
                res[level].append(node.val)
                util(node.left, level + 1)
                util(node.right, level + 1)
                
        util(root, 0)
        
        return res