import sys
from collections import deque
input = sys.stdin.readline

# 크기 커지는지 확인
def level_up(shark_size, exp):
    if shark_size == exp:
        shark_size += 1
        exp = 0
        
    return shark_size, exp

# 물고기들과의 거리 확인
def distance_from_fish(shark_x, shark_y, fish_x, fish_y):
    dq = deque()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dq.append((shark_x, shark_y))
    visited[shark_x][shark_y] = 1
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    while dq:
        x, y = dq.popleft()
        
        if x == fish_x and y == fish_y:
            return visited[x][y] - 1
        
        for i in range(4):
            nx = x + dx[i]    
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] <= shark_size and visited[nx][ny] == 0:
                dq.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
        
    return -1

# 물고기 위치 확인
def fishes_pos():
    tmp_list = []
    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] < 7:
                tmp_list.append((i, j))
    return tmp_list

# 맵 크기, 상어 위치, 크기 등 초기값 설정
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            shark = i, j

shark_size = 2
exp = 0
answer = 0


while True:
    # 물고기 위치 확인 없으면 종료
    fishes = fishes_pos()
    if len(fishes) == 0:
        break
    fishes_dis = []
    dis = float('inf')
    target = None
    
    # 최단 거리 물고기 확인
    for fish in fishes:
        tmp = distance_from_fish(*shark, *fish)
        fishes_dis.append(tmp)
        if arr[fish[0]][fish[1]] < shark_size and 0 < tmp < dis:
            target = fish
            dis = tmp

    # 먹을 물고기 없으면 종료
    if target == None:
        break
    # 먹을 수 있는 물고기면 먹고 이동
    else:
        arr[shark[0]][shark[1]] = 0
        arr[target[0]][target[1]] = 9
        exp += 1
        shark_size, exp = level_up(shark_size, exp)
        shark = target
        answer += dis
        
print(answer)


# 먹을 수 있는 물고기 위치와 거리를 bfs로 한번에 구하면 시간복잡도를 줄일 수 있다
