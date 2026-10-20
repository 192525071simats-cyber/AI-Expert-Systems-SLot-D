
import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('F', 4)],
    'E': [('F', 1)],
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

pq = [(heuristic[start], 0, start, [start])]
best_cost = {start: 0}

while pq:
    f, g, node, path = heapq.heappop(pq)

    if node == goal:
        print("Optimal path:", path)
        print("Total cost:", g)
        break

    if g > best_cost.get(node, float('inf')):
        continue

    for neighbor, cost in graph[node]:
        new_g = g + cost

        if new_g < best_cost.get(neighbor, float('inf')):
            best_cost[neighbor] = new_g
            new_f = new_g + heuristic[neighbor]

            heapq.heappush(
                pq,
                (new_f, new_g, neighbor, path + [neighbor])
            )
else:
    print("No path found")
