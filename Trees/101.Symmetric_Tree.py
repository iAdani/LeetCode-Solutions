# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symmetric(p, q) -> bool:
            if not p and not q:
                return True
            
            if not p or not q or p.val != q.val:
                return False
            
            return symmetric(p.left, q.right) and symmetric(p.right, q.left)

        return symmetric(root.right, root.left)
