from collections import deque
# 오른쪽 위 왼쪽 아래
way = [(0,1),(-1,0),(0,-1),(1,0)]
n,m,K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
# 오른쪽 위 왼쪽 아래
rounds = [(x,0,0) for x in range(n)] + [(n-1,x,1) for x in range(n)] + [(x,n-1,2) for x in range(n-1,-1,-1)] + [(0,x,3) for x in range(n-1, -1 ,-1)]
rounds = rounds * (K//(4*n)+1)
# BFS: 각 팀별 이동루트 구하기(0이 아닌 경우)
teams_route = [] # 각 팀별 이동루트
teams_start = [0]*m # 머리의 위치
teams_current = [] # 각 팀별 인원들의 위치
teams_way = [-1]*m # 각 팀별 이동방향
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        # 1인 경우에 시작
        if field[i][j] == 1 and not visited[i][j]:
            queue = deque()
            queue.append((i,j,1))
            temp, current = [(i,j)], [(i,j)]
            visited[i][j] = 1
            while queue:
                x,y,value = queue.popleft()
                for k in range(4):
                    nx = x + way[k][0]
                    ny = y + way[k][1]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == 1:
                        continue
                    # 같거나 1보다 큰 경우에만 추가
                    if field[nx][ny] == value or field[nx][ny] == value + 1:
                        visited[nx][ny] = 1
                        queue.append((nx,ny, field[nx][ny]))
                        temp.append((nx,ny))
                        if field[nx][ny] != 4:
                            current.append((nx,ny))
            # 완성된 루트 삽입
            teams_route.append(temp)
            teams_current.append(current)
# K번의 라운드 진행
scores = [0]*m
for round in range(K):
    # 각 팀별 이동
    for i in range(m):
        start = (teams_start[i] + teams_way[i])% len(teams_route[i])
        teams_current[i] =  [teams_route[i][start]]+ teams_current[i][:-1]
        teams_start[i] = start
    # 점수 획득 판정 시작
    x,y,dir = rounds[round]
    flag = 0
    get_score = -1,-1 # 팀 번호, 점수 획득한 팀원 순서
    for i in range(n):
        nx = x + i*way[dir][0]
        ny = y + i*way[dir][1]
        # 점수 획득할 수 있는지 체크
        for j in range(m):
            if (nx,ny) in teams_current[j]:
                get_score = j, teams_current[j].index((nx,ny))
                flag = 1
                break
        if flag:
            break
    if get_score[0] != -1:
        scores[get_score[0]] += (get_score[1] + 1)**2
        teams_current[get_score[0]] = teams_current[get_score[0]][::-1]
        teams_start[get_score[0]] = teams_route[get_score[0]].index(teams_current[get_score[0]][0])
        teams_way[get_score[0]] *= -1
print(sum(scores))
# 소요시간 약 1시간 30분
# 각 팀별 이동루트를 구한 다음에 매번이동시키면서 점수를 획득할 수 있는지 체크해야 함