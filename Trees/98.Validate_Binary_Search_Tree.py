# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(root, min_val, max_val):
            if not root:
                return True
            
            if root.val <= min_val or root.val >= max_val:
                return False
            
            if not DFS(root.left, min_val, root.val):
                return False

            return DFS(root.right, root.val, max_val)
        
        return DFS(root, float('-inf'), float('inf'))