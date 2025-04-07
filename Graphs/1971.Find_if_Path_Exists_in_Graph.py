class Solution:
    # O(V + E)
    # DFS
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph, visited = defaultdict(set), set()
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        def DFS(curr):
            visited.add(curr)
            if destination in graph[curr]:
                return True
            
            for neighbor in graph[curr]:
                if neighbor not in visited and DFS(neighbor):
                    return True

            return False
            
        return DFS(source)
        