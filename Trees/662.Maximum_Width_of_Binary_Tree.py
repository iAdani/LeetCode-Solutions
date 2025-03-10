# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        widest = 1
        queue = [(root, 1)]
        while queue:
            next_queue = []
            for node, pos in queue:
                if node.left:
                    next_queue.append((node.left, 2 * pos))
                if node.right:
                    next_queue.append((node.right, 2 * pos + 1))
            
            if next_queue:
                widest = max(widest, next_queue[-1][1] - next_queue[0][1] + 1)

            queue = next_queue
                
        
        return widest

