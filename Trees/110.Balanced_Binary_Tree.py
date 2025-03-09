# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def find_height(root) -> int:
            if not root or not self.balanced:
                return 0

            right = find_height(root.right)
            if not self.balanced:
                return 0
            
            left = find_height(root.left)
            if abs(right - left) > 1:
                self.balanced = False

            return 1 + max(right, left)
        
        find_height(root)
        return self.balanced
        
        