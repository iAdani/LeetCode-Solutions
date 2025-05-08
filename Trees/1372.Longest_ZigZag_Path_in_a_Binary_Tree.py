# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(N), Space: O(N)
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def DFS(node, is_left, curr):
            if not node:
                return
            
            ans[0] = max(ans[0], curr)

            if is_left:
                DFS(node.right, False, curr + 1)
                DFS(node.left, True, 1)
            else:
                DFS(node.right, False, 1)
                DFS(node.left, True, curr + 1)
        
        DFS(root, True, 0)
        return ans[0]
        