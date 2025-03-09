# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0

        def find_height(root) -> int:
            if not root:
                return 0
            
            right = find_height(root.right)
            left = find_height(root.left)

            self.longest = max(self.longest, right + left)
            
            return 1 + max(right, left)
        
        find_height(root)
        return self.longest
