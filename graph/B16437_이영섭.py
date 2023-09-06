import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
island = [[0, 0], [0, 0]]
path = [[] for _ in range(N+1)]

for i in range(2, N+1):
    t, a, p = input().split()
    island.append([t, int(a)])
    path[int(p)].append(i)


def dfs(idx):
    ans = 0
    for i in path[idx]:
        ans += dfs(i)
    if island[idx][0] == 'W':
        ans -= island[idx][1]
        if ans < 0:
            ans = 0
    elif island[idx] != 0:
        ans += island[idx][1]
    return ans


print(dfs(1))