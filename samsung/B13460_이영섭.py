import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def move(x, y, dx, dy):
    cnt = 0
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs():
    while dq:
        rx, ry, bx, by, depth = dq.popleft()
        if depth >= 10:
            return -1
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if arr[nbx][nby] != 'O':
                if arr[nrx][nry] == 'O':
                    return depth+1
                if visit[nrx][nry][nbx][nby]:
                    continue
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                visit[nrx][nry][nbx][nby] = 1
                dq.append((nrx, nry, nbx, nby, depth+1))
    return -1

N, M = map(int, input().split())
arr = [list(map(str, input().rstrip())) for _ in range(N)]
visit = [[[[0 for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)]
dq = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j

dq.append((rx, ry, bx, by, 0))
visit[rx][ry][bx][by] = 1
print(bfs())

# 문제 접근 방법
# # 지금까지 생각해야 할 정점이 1개였다면 이번에는 2개
# # visit을 이차원 배열이 아니라 사차원 배열로 만들어 한번에 관리
# # 구슬들이 몇 번 이동하여 현 지점에 와 있는지를 depth를 이용하여 파악
# 새로 배운 python
# # map에 str 함수를 사용하여 형태를 유지, list함수를 썼다가 rx, ry, bx, by에서 계속 오류 뱉음
# # main 안부르고 함수로 만든 뒤에 print로 감싸면 편함