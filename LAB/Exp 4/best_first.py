
import heapq

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

pq = [(heuristic[start], start)]
visited = set()
parent = {start: None}

while pq:
    _, node = heapq.heappop(pq)

    if node in visited:
        continue

    visited.add(node)

    if node == goal:
        break

    for neighbor in graph[node]:
        if neighbor not in visited:
            parent.setdefault(neighbor, node)
            heapq.heappush(pq, (heuristic[neighbor], neighbor))

if goal in visited:
    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()
    print("Path found:", path)
else:
    print("No path found")
