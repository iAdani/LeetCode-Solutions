# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq

class Solution:
    # O(n * log(k))
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []

        def DFS(root):
            if not root:
                return
            
            heapq.heappush(heap, -root.val)
            if len(heap) > k:
                heapq.heappop(heap)
            
            DFS(root.left)
            DFS(root.right)
        
        DFS(root)
        return -heap[0]
    

    # O(N)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0]
        K = [k]

        def DFS(root):
            if not root:
                return

            DFS(root.left)

            if K[0] == 1:
                res[0] = root.val
            
            K[0] -= 1
            if K[0] > 0:
                DFS(root.right)
        
        DFS(root)
        return res[0]
