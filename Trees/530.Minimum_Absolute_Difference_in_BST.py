# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(N)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minn = [100001]
        last = [None]

        def DFS(root):
            if not root:
                return

            DFS(root.left)
            if last[0] != None:
                minn[0] = min(minn[0], root.val - last[0])

            last[0] = root.val
            DFS(root.right)

        DFS(root)
        return minn[0]

