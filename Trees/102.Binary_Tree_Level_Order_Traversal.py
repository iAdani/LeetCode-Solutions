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
            
        curr_lvl, res = [root], []
        while curr_lvl:
            next_lvl = []
            for node in curr_lvl:
                if node.left:
                    next_lvl.append(node.left)
                if node.right:
                    next_lvl.append(node.right)
            
            res.append([node.val for node in curr_lvl])
            curr_lvl = next_lvl
        
        return res
        