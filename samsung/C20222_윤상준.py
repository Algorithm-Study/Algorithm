from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for _ in range(4):
    color = 1
    visited = [[0] * N for _ in range(N)]
    # 그룹 구하기
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque()
                queue.append((i,j))
                team_num = field[i][j]
                visited[i][j] = color
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] == team_num:
                            queue.append((nx, ny))
                            visited[nx][ny] = color
                color += 1
    cnt = [0] * color
    edges = [[0] * color for _ in range(color)]
    num = [0] * color
    new_visited = [[0] * N for _ in range(N)]
    # 우리팀 칸 수, 다른 팀과의 변 수, 우리 팀 번호 찾기
    for i in range(N):
        for j in range(N):
            if not cnt[visited[i][j]]:
                group_num = visited[i][j]
                queue = deque()
                queue.append((i,j))
                cnt[group_num] += 1
                num[group_num] = field[i][j]
                new_visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N and not new_visited[nx][ny]:
                            if group_num == visited[nx][ny]:
                                queue.append((nx, ny))
                                cnt[group_num] += 1
                                new_visited[nx][ny] = 1
                            else:
                                edges[group_num][visited[nx][ny]] += 1
    # 이번 회차 점수 계산
    for i in range(1, color):
        for j in range(i + 1, color):
            answer += (cnt[i] + cnt[j]) * num[i] * num[j] * edges[i][j]
    # 종료 조건(시간 조금 줄이기)
    if _ == 3:
        break
    temp = [[0] * N for _ in range(N)]
    # 십자가 돌리기
    for i in range(N):
        temp[i][N // 2] = field[N // 2][N -1 -i]
        temp[N // 2][i] = field[i][N // 2]
    # 90도 돌리기
    for x,y in [(0,0), (0,N // 2 + 1), (N // 2 + 1, 0), (N // 2 + 1, N // 2 + 1)]:
        for i in range(N // 2):
            for j in range(N // 2):
                temp[x+i][y+j] = field[x + N // 2 - 1 - j][y + i]
    field = temp
print(answer)