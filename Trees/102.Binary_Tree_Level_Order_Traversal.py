# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue, next_queue = [root], []
        result = []
        while queue:
            for i in range(len(queue)):
                if queue[i].left:
                    next_queue.append(queue[i].left)
                if queue[i].right:
                    next_queue.append(queue[i].right)
                queue[i] = queue[i].val
            
            result.append(queue)
            queue = next_queue
            next_queue = []
        
        return result
        