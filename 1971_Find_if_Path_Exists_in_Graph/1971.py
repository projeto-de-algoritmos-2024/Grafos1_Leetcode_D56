from collections import deque, defaultdict

def validPath(n, edges, source, destination):
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = set()
    visited.add(source)

    while queue:
        current = queue.popleft()

        if current == destination:
            return True

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5

print(validPath(n, edges, source, destination))