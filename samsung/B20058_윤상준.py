#python3 시간 초과
#pypy3 124672KB / 812ms
from collections import deque
#기본 설정
N, Q = map(int, input().split())
length = 2**N
field = [list(map(int, input().split())) for _ in range(length)]
operation = list(map(int,input().split()))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for op in operation:
    # 회전시키기
    square = 2**op
    for l in range(square, length+1, square):
        for i in range(square, length+1, square):
            temp = [[0]*square for _ in range(square)]
            for j in range(l-square, l):
                for k in range(i-square, i):
                    temp[k - (i - square)][square - (j - (l - square)) - 1] = field[j][k]
            #for m in range(square):
            #    print(temp[m])
            for j in range(l-square, l):
                for k in range(i-square, i):
                    field[j][k] = temp[j - (l - square)][k - (i - square)]
    # 녹는지 체크
    temp = [field[x][:] for x in range(length)]
    for i in range(length):
        for j in range(length):
            count = 0
            if field[i][j] == 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= length or ny >= length or field[nx][ny] == 0:
                    continue
                count += 1
            if count < 3:
                temp[i][j] -= 1
    for i in range(length):
        field[i] = temp[i][:]
# 전체 얼음량 계산
total_ice = sum(map(sum, field))
print(total_ice)
#최대 덩어리 계산
visited = [[False]*length for _ in range(length)]
queue = deque()
max_count = 0
for i in range(length):
    for j in range(length):
        count = 0
        if visited[i][j] or field[i][j] == 0:
            continue
        queue.append([i, j])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            count += 1
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= length or ny >= length or visited[nx][ny]:
                    continue
                if field[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
        max_count = max(max_count, count)
print(max_count)

