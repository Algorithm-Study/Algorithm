from collections import deque
k = int(input())
w,h = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
kx = [-2, -2, -1, -1, 1, 1, 2, 2]
ky = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
queue = deque()
queue.append([0,0,k,0])
visited[0][0][k] = 1
while queue:
    y, x, kmove, count = queue.popleft()
    if y == h-1 and x == w-1:
        print(count)
        exit()
    if kmove > 0:
        for i in range(8):
            nx = x + kx[i]
            ny = y + ky[i]
            if nx < 0 or ny < 0 or nx >= w or ny >=h or visited[ny][nx][kmove -1] == 1 or field[ny][nx] != 0:
                continue
            visited[ny][nx][kmove -1] = 1
            queue.append([ny,nx, kmove-1, count+1])
    for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= w or ny >=h or visited[ny][nx][kmove] == 1 or field[ny][nx] != 0:
                continue
            visited[ny][nx][kmove] = 1
            queue.append([ny,nx, kmove, count+1])
print(-1)
#빠르게 도착만 하면 된다고 생각해서 field 내에서 방문 처리를 해서 해결하려고 했지만 실패
#말처럼 이동을 몇번 하는냐에 따라서 달라질 수 있기 때문에 따로 방문 처리를 해야 문제가 풀리는 것으로 예상