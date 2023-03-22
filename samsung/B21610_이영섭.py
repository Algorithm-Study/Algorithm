from collections import deque
import sys
input = sys.stdin.readline

def water_copy_bug():
    for tp in temp:
        for i in [1, 3, 5, 7]:
            nx = tp[0] + dx[i]
            ny = tp[1] + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if arr[nx][ny] != 0:
                arr[tp[0]][tp[1]] += 1

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1] # 1부터 8까지

N, M = map(int, input().split())
arr = [[0 for _ in range(N)] for _ in range(N)]
cloud = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(M):
    di, si = map(int, input().split())
    di -= 1
    temp = deque()
    temp_list = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(len(cloud)):
        x, y = (dx[di]*si + cloud[j][0])%N, (dy[di]*si + cloud[j][1])%N
        arr[x][y] += 1
        temp.append((x, y))
        temp_list[x][y] = 1
    water_copy_bug()
    cloud = deque()
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and temp_list[i][j] == 0:
                cloud.append((i, j))
                arr[i][j] -= 2

answer = 0
for i in arr:
    answer += sum(i)
print(answer)

# 문제 접근 방식
# # 구현 문제이므로 조건을 읽고 풀면 된다.
# # 시간초과 이슈가 있었으나(in/not in은 시간 복잡도가 O(N)) 
# # i, j의 idx값으로 접근할 수 있는 temp_list를 check하는 방식으로 해결