class Solution:
    # O(n + m)
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, value in enumerate(values):
            a, b = equations[i]
            graph[a][b] = value
            graph[b][a] = 1 / value

        def DFS(node, target, curr, visited):
            if node not in graph or target not in graph:
                return -1
            if node == target:
                return 1

            if target in graph[node]:
                return curr * graph[node][target]
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    res = DFS(neighbor, target, curr * graph[node][neighbor], visited)
                    if res != -1:
                        return res
                    
            return -1

        ans = []
        for a, b in queries:
            ans.append(DFS(a, b, 1, set()))

        return ans
