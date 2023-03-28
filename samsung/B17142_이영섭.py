from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus = []
d_virus, full_virus, block = 0, 0, 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
            d_virus += 1
        elif arr[i][j] == 1:
            block += 1
full_virus = N*N - block
bf = list(combinations(virus, M))
def bfs(board, visit, case):
    v_cnt = d_virus
    # print(v_cnt)
    dq = deque()
    for cs in case:
        dq.append(cs)
        visit[cs[0]][cs[1]] = 0
    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if board[nx][ny] == 1 or visit[nx][ny] > -1: continue
            if board[nx][ny] == 0:
                v_cnt += 1
            dq.append((nx, ny))
            visit[nx][ny] = visit[cx][cy] + 1
            if v_cnt == full_virus:
                # print(max(map(max, visit)))
                return max(map(max, visit))
    return -1

def solution():
    min_time = 10000
    cnt = 0
    if d_virus == full_virus:
        return 0
    for case in bf:
        new_arr = copy.deepcopy(arr)
        visit = [[-1 for _ in range(N)] for _ in range(N)]
        time = bfs(new_arr, visit, case)
        if time == -1:
            cnt += 1
        elif min_time > time:
            min_time = time
    if cnt == len(bf):
        return -1
    return min_time

print(solution())

# 문제 접근 방식
# # 바이러스 활성화되는 모든 경우의 수를 탐색
# # board에 존재하는 바이러스 수가 full_virus와 같아지면 board의 최고값을 return
# # 덱이 비었음에도 full_virus보다 바이러스 수가 적다면 -1을 return
# 새로 배운 python
# # max(map(max, visit))을 사용하면 이차원 배열의 최댓값을 구할 수 있다.