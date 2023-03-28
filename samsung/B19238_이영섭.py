from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
row, column = map(int, input().split())
row, column = row-1, column-1
client = {}

for i in range(2, M+2):
    cusx, cusy, desx, desy = map(int, input().split())
    cusx, cusy, desx, desy = cusx-1, cusy-1, desx-1, desy-1
    client[(cusx, cusy)] = (desx, desy)
    arr[cusx][cusy] = i
    arr[desx][desy] = i + 400

def find_client(x, y, c_fuel):
    dq = deque()
    dq.append([x, y, c_fuel])
    visit = [[0 for _ in range(N)] for _ in range(N)]
    while dq:
        cx, cy, fuel = dq.popleft()
        if fuel == 0:
            return [cx, cy, -1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == 1 or visit[nx][ny]: continue
            if arr[nx][ny] != 0 and arr[nx][ny] != 0 and arr[nx][ny]//100 == 0:
                arr[nx][ny] = 0
                return [nx, ny, fuel-1]
            dq.append([nx, ny, fuel-1])
            visit[nx][ny] = 1
    return [0, 0, -1]

def find_destination(x, y, c_fuel):
    dq = deque()
    dq.append([x, y, c_fuel])
    des_x, des_y = client[(x, y)][0], client[(x, y)][1]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    while dq:
        cx, cy, fuel = dq.popleft()
        if fuel == 0:
            return [cx, cy, -1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if arr[nx][ny] == 1 or visit[nx][ny]: continue
            visit[nx][ny] = visit[cx][cy] + 1
            if nx == des_x and ny == des_y:
                arr[nx][ny] = 0
                fuel += visit[nx][ny]*2
                return [nx, ny, fuel-1]
            dq.append([nx, ny, fuel-1])
    return [0, 0, -1]

def no_fuel(nf):
    if nf == -1:
        return True
    else:
        return False

def solution():
    nr, nc, nf = find_client(row, column, fuel)
    if no_fuel(nf): return -1
    nr, nc, nf = find_destination(nr, nc, nf)
    if no_fuel(nf): return -1
    for i in range(M-1):
        nr, nc, nf = find_client(nr, nc, nf)
        if no_fuel(nf): return -1
        nr, nc, nf = find_destination(nr, nc, nf)
        if no_fuel(nf): return -1
    return nf

print(solution())