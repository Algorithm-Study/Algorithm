import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
visited = [[0 for _ in range(m)] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x,y):
    if visited[x][y] == 1:
        return dp[x][y]
    
    if x == n-1 and y == m-1:
        return 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[x][y]:
                dp[x][y] += dfs(nx, ny)
    visited[x][y] = 1
    return dp[x][y]

print(dfs(0,0))
'''
4 4
16 9 8 1
15 10 7 2
14 11 6 3
13 12 5 4
>> 10

4 4
20 19 18 17
10 9 8 16
100 100 7 15
100 100 6 14
>> 1
'''