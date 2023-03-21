import sys
input = sys.stdin.readline

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
dq = deque()
dq.append((r, c, d))
data[r][c] = -1

def answer():
    ans = 0
    for row in data:
        for col in row:
            if col == -1:
                ans += 1
    return ans

def bfs():
    while dq:
        cx, cy, cd = dq.popleft()
        cnt = 0
        for _ in range(4):
            cd = (cd + 3) % 4
            nx = cx + dx[cd]
            ny = cy + dy[cd]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or data[nx][ny] == 1 or data[nx][ny] == -1:
                cnt += 1
                continue
            else:
                dq.append((nx, ny, cd))
                data[nx][ny] = -1
                break
        if cnt == 4:
            tc = (cd + 2) % 4
            nx = cx + dx[tc]
            ny = cy + dy[tc]
            if data[nx][ny] == 1:
                ans = answer()
                return ans
            dq.append((nx, ny, cd))
    ans = answer()
    return ans
print(bfs())


# 문제 접근 방법
# # 일반적인 bfs인데 단 방향인 bfs
# # 단 주위에 진행할 곳이 없으면 후진
