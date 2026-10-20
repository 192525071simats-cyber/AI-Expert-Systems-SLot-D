
from collections import deque

capacity_a = 4
capacity_b = 3
target = 2

start = (0, 0)
queue = deque([(start, [])])
visited = set()

while queue:
    (a, b), path = queue.popleft()

    if (a, b) in visited:
        continue

    visited.add((a, b))
    path = path + [(a, b)]

    if a == target or b == target:
        print("Solution found:")
        for state in path:
            print(state)
        break

    states = [
        (capacity_a, b),                  # Fill jug A
        (a, capacity_b),                  # Fill jug B
        (0, b),                           # Empty jug A
        (a, 0),                           # Empty jug B
        (a - min(a, capacity_b - b),
         b + min(a, capacity_b - b)),     # Pour A into B
        (a + min(b, capacity_a - a),
         b - min(b, capacity_a - a))      # Pour B into A
    ]

    for state in states:
        if state not in visited:
            queue.append((state, path))
else:
    print("No solution found")
