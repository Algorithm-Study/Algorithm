import sys
input =sys.stdin.readline
r, c = map(int, input().split())
field = [input() for _ in range(r)]
visited = [0]*(ord('Z')-ord('A') + 1)
dx = [-1, 0 ,1 ,0]
dy = [0, -1, 0, 1]
visited[ord(field[0][0])-ord('A')] = 1
max_visit = 1
def dfs(x,y, count):
    global max_visit
    max_visit = max(max_visit, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >=c or visited[ord(field[nx][ny])-ord('A')] == 1:
            continue
        visited[ord(field[nx][ny])-ord('A')] = 1
        dfs(nx, ny, count+1)
        visited[ord(field[nx][ny])-ord('A')] = 0
    return max_visit

print(dfs(0,0,1))
# 메모리 제약, 시간 제약이 python에게 매우 가혹한 문제
# BFS 활용 시 통과하지 못해서 DFS 방식으로 변경
# 기존에 0,0,0 시작 이후 1 더한 것을 0,0,1로 변경하니 통과