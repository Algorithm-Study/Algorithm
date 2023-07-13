N = int(input())
data = list(map(int, input().split()))
grad = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j:
            grad[i][j] = (data[i] - data[j]) / (i - j)

ans = [0] * N
for i in range(N):
    cnt = 0
    for j in range(i):
        can = True
        for k in range(j+1, i):
            if grad[k][i] <= grad[j][i]:
                can = False
        if can:
            cnt += 1
    for j in range(i+1, N):
        can = True
        for k in range(i+1, j):
            if grad[i][k] >= grad[i][j]:
                can = False
        if can:
            cnt += 1
    ans[i] = cnt
print(max(ans))
