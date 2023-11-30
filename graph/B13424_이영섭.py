T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[int(1e9)]*N for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
    K = int(input())
    friend = list(map(int, input().split()))

    for k in range(N):
        graph[k][k] = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    ans, idx = float('inf'), 0
    for i in range(N):
        summ = sum(graph[i][f-1] for f in friend)
        if ans > summ:
            ans = summ
            idx = i
    print(idx+1)
