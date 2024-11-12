from collections import deque, defaultdict

def findShortestCycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        queue = deque([(start, -1)]) 
        visited = set()

        while queue:
            node, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited: 
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    
                    print(f"Ciclo encontrado começando em {start}")
                    return True
        return False
    
    
    for i in range(n):
        if bfs(i):
            return "Ciclo encontrado"
    return "Sem ciclo"

n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]

print(findShortestCycle(n, edges))