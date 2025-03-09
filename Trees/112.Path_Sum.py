# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def find_sum(root, summ):
            if not root:
                return False
            
            summ += root.val
            if not root.left and not root.right:
                return summ == targetSum

            return find_sum(root.right, summ) or find_sum(root.left, summ)
        
        return find_sum(root, 0)

