class Solution:
    # O(N^2)
    def goodNodes(self, root: TreeNode) -> int:
        stack = [root.val]
        count = [1]

        def DFS(root):
            if not root:
                return
            if max(stack) <= root.val:
                count[0] += 1
            
            stack.append(root.val)
            DFS(root.left)
            DFS(root.right)
            stack.pop()

        DFS(root.left)
        DFS(root.right)
        return count[0]
