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


    # O(N)
    def goodNodes(self, root: TreeNode) -> int:
        def DFS(root, curr_max):
            if not root:
                return 0

            next_max = max(root.val, curr_max)
            good = DFS(root.left, next_max)
            good += DFS(root.right, next_max)

            return 1 + good if root.val >= curr_max else good

        return DFS(root, root.val)