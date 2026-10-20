
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 4)],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'

pq = [(0, start, [start])]
visited = set()

while pq:
    cost, node, path = heapq.heappop(pq)

    if node == goal:
        print("Least-cost path:", path)
        print("Total cost:", cost)
        break

    if node not in visited:
        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (cost + edge_cost, neighbor, path + [neighbor])
                )
