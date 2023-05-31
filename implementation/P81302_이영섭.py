from collections import deque

di = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(p):
    for i in range(5):
        for j in range(5):
            if p[i][j] == 'P':
                
                dq = deque()
                dq.append((i, j))
                visit = [[0]*5 for _ in range(5)]
                dist = [[0]*5 for _ in range(5)]
                visit[i][j] = 1
                
                while dq:
                    cx, cy = dq.popleft()
                    for dir in range(4):
                        nx, ny = cx + di[dir][0], cy + di[dir][1]
                        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                            continue
                        if visit[nx][ny] == 1:
                            continue
                        if p[nx][ny] == 'O':
                            dq.append((nx, ny))
                            visit[nx][ny] = 1
                            dist[nx][ny] = dist[cx][cy] + 1
                        if p[nx][ny] == 'P' and dist[cx][cy] <= 1:
                            return 0
    return 1

def solution(places):
    answer = []
    for p in places:
        ret = bfs(p)
        if ret:
            answer.append(1)
        else:
            answer.append(0)
    return answer