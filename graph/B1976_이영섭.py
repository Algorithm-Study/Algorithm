N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N))
plan = list(map(int, input().split()))


def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            union(i, j)

ans = "YES"
for i in range(1, M):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        ans = "NO"
        break
print(ans)
