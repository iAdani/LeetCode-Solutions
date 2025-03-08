# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, length):
        if not node:
            return length
        
        return max(self.DFS(node.left, length + 1), self.DFS(node.right, length + 1))
    
    # O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, 0)