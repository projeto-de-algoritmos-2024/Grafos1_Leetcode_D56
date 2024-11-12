from collections import deque, defaultdict

def findShortestCycle(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(start):
        queue = deque([(start, 0, -1)])
        distances = {start: 0}
        
        while queue:
            node, dist, parent = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in distances:
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1, node))
                elif neighbor != parent:
                    cycle_length = dist + 1
                    return cycle_length
        return float('inf')
    
    
    shortest_cycle = float('inf')
    for i in range(n):
        shortest_cycle = min(shortest_cycle, bfs(i))
    return -1 if shortest_cycle == float('inf') else shortest_cycle

n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]

print(findShortestCycle(n, edges))