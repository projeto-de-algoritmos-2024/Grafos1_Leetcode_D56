from collections import deque, defaultdict

def findShortestCycle(self,n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    shortest_cycle = float('inf')
    for i in range(n):
        queue = deque([(i, 0, -1)])
        distances = [-1] * n
        distances[i] = 0
        
        while queue:
            node, dist, parent = queue.popleft()
            for neighbor in graph[node]:
                if distances[neighbor] == -1: 
                    distances[neighbor] = dist + 1
                    queue.append((neighbor, dist + 1, node))
                elif neighbor != parent:
                    cycle_length = distances[node] + distances[neighbor] + 1
                    shortest_cycle = min(shortest_cycle, cycle_length)
    return -1 if shortest_cycle == float('inf') else shortest_cycle

n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]

print(findShortestCycle(object,n, edges))