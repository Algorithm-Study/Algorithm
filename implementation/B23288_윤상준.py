from collections import deque
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] 
# 각 방향 별 위치별 이동 결과
moving_after = [[3, 0, 2, 5, 4, 1],[4, 1, 0, 3, 5, 2], [1, 5, 2, 0, 4, 3],[2, 1, 5, 3, 0, 4]]
uturn = {0:2, 1:3, 2:0, 3:1}
n,m,K = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))
x, y = 0,0
dice = [6, 4, 2, 3, 5, 1]
way = 0
score = 0
for _ in range(K):
    # 주사위 이동
    nx = x + dx[way]
    ny = y + dy[way]
    # 막다른 곳이면 반대로 이동
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        way = way ^ 2
        nx = x + dx[way]
        ny = y + dy[way]
        
    # 점수 얻기
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    queue.append((nx,ny))
    visited[nx][ny] = 1
    count = 1
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            # 범위를 벗어낫거나 방문한 적이 있는 경우
            if na < 0 or nb < 0 or na >= n or nb >= m or visited[na][nb]:
                continue
            # 같은 값을 가지는 경우
            if field[na][nb] == field[a][b]:
                count += 1
                visited[na][nb] = 1
                queue.append((na,nb))
    score += field[nx][ny] * count
    # 주사위 회전
    new_dice = dice[:]
    for i in range(6):
        new_dice[i] = dice[moving_after[way][i]]
    dice = new_dice[:]
    # 회전 방향 갱신
    # 1. 주사위 아랫면이 큰 경우
    if dice[0] > field[nx][ny]: 
        way = (way+1)%4
    # 2. 주사위 아랫면이 작은 경우
    elif dice[0] < field[nx][ny]:
        way = (way-1)%4
    # 위치 갱신
    x = nx
    y = ny
print(score)