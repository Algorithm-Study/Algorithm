import sys
input = sys.stdin.readline

from collections import deque

def solution():
    M, N, H = map(int, input().split())

    dq = deque()

    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    arr = [[[0 for _ in range(H)] for _ in range(M)] for _ in range(N)]
    visit = [[[0 for _ in range(H)] for _ in range(M)] for _ in range(N)]

    for k in range(H):
        for i in range(N):
            temp = list(map(int, input().split()))
            for j in range(M):
                arr[i][j][k] = temp[j]
                if temp[j] == 1:
                    dq.append([i, j, k])
                    visit[i][j][k] = 1
                elif temp[j] == -1:
                    visit[i][j][k] = -1
    
    # if bool(dq) == False:
    #     print(0)
    #     return
    
    while bool(dq) == True:
        i, j, k = dq.popleft()
        for idx in range(len(dx)):
            nx = dx[idx] + i
            ny = dy[idx] + j
            nz = dz[idx] + k
            if nx < 0 or ny < 0 or nz < 0 or nx >= N or ny >= M or nz >= H:
                continue
            if arr[nx][ny][nz] != 0 or visit[nx][ny][nz] != 0 :
                continue
            visit[nx][ny][nz] = visit[i][j][k] + 1
            arr[nx][ny][nz] = 1
            dq.append([nx, ny, nz])
    max_val = 0
    for i in range(N):
        for j in range(M):
            for k in range(H):
                if visit[i][j][k] == 0:
                    print(-1)
                    return
                if visit[i][j][k] > max_val:
                    max_val = visit[i][j][k]
    print(max_val - 1)
    
if __name__ == "__main__":
    solution()
    
# 문제 접근 방법
# # bfs의 정석
# # dq가 비었을 때, 0을 출력하고 return하는 것에 문제가 있음