# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(n * m), Space: O(n + m)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root, sub):
            if not root or not sub:
                return root == sub

            return root.val == sub.val and isEqual(root.right, sub.right) and isEqual(root.left, sub.left)

        def DFS(root):
            if not root:
                return False

            return isEqual(root, subRoot) or DFS(root.right) or DFS(root.left)

        return DFS(root)
    

    # Time: O(n + m), Space: O(n + m)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return '#'

            return f'({node.val},{serialize(node.left)}, {serialize(node.right)})'
        
        root_serial = serialize(root)
        sub_serial = serialize(subRoot)

        return sub_serial in root_serial
