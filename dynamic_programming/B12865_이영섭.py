N, K = map(int, input().split())
goods = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
knapsack = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if j < goods[i][0]:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - goods[i][0]] + goods[i][1], knapsack[i - 1][j])

print(knapsack[N][K])
