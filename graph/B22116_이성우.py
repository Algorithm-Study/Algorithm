import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input().rstrip())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visited = [[INF for _ in range(n)] for _ in range(n)]

def dijkstra(i, j):
    q = []
    heapq.heappush(q, (0, i, j))
    visited[i][j] = 0
    while q:
        s, x, y = heapq.heappop(q)
        if visited[x][y] < s:
            continue
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                ns = max(s, abs(arr[nx][ny]-arr[x][y]))
                if visited[nx][ny] > ns:
                    visited[nx][ny] = ns
                    heapq.heappush(q, (ns, nx, ny))
                    
dijkstra(0, 0)
print(visited[n-1][n-1])