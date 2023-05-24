from collections import deque

N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]
dt = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    dq = deque()
    temp = []
    dq.append((x, y))
    temp.append((x, y))
    while dq:
        cx, cy = dq.popleft()
        for dir in dt:
            nx, ny = cx + dir[0], cy + dir[1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visit[nx][ny] == 1:
                continue
            if L <= abs(people[nx][ny] - people[cx][cy]) <= R:
                visit[nx][ny] = 1
                dq.append((nx, ny))
                temp.append((nx, ny))
    return temp


day = 0
while True:
    visit = [[0]*N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                country_list = bfs(i, j)
                if len(country_list) > 1:
                    flag = 1
                    number = sum([people[x][y] for x, y in country_list]) // len(country_list)
                    for x, y in country_list:
                        people[x][y] = number
    if flag == 0:
        break
    day += 1
print(day)