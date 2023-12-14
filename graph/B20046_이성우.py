import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
arr = [list(map(int ,input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    distance = [[INF for _ in range(m)] for _ in range(n)]
    distance[0][0] = arr[0][0]
    q = []
    if distance[0][0] == -1:
        return INF
    else:
        heapq.heappush(q, [distance[0][0], 0, 0])
        
    while q:
        cost, x, y = heapq.heappop(q)
        
        if distance[x][y] < cost:
            continue
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                next_ = arr[nx][ny]
                if next_ != -1 and distance[nx][ny] > cost + next_:
                    distance[nx][ny] = cost + next_
                    heapq.heappush(q, [cost+next_, nx, ny])
                    
    return distance[n-1][m-1]

answer = dijkstra()
if answer == INF:
    print(-1)
else:
    print(answer)
                    