"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    # O(V + E)
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copies = {}
        def DFS(node):
            if node.val in copies:
                return copies[node.val]
            
            copy = Node(node.val)
            copies[node.val] = copy
            copy.neighbors = [DFS(n) for n in node.neighbors]

            return copy
        
        return DFS(node)
