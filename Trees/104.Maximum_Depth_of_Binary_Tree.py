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
        
        return 1 +  max(self.DFS(node.left, length), self.DFS(node.right, length))
    
    # O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, 0)
    
    # O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))