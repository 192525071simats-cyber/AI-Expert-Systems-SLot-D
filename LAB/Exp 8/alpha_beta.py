
def alphabeta(depth, node, maximizing, alpha, beta, values):
    if depth == 2:
        return values[node]

    if maximizing:
        best = float('-inf')

        for child in [node * 2, node * 2 + 1]:
            best = max(
                best,
                alphabeta(depth + 1, child, False,
                          alpha, beta, values)
            )
            alpha = max(alpha, best)

            if beta <= alpha:
                print("Branch pruned")
                break

        return best

    else:
        best = float('inf')

        for child in [node * 2, node * 2 + 1]:
            best = min(
                best,
                alphabeta(depth + 1, child, True,
                          alpha, beta, values)
            )
            beta = min(beta, best)

            if beta <= alpha:
                print("Branch pruned")
                break

        return best


values = [3, 5, 2, 9]

result = alphabeta(
    0, 0, True, float('-inf'), float('inf'), values
)

print("Best value using Alpha-Beta:", result)
