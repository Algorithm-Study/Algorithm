# 환경 설정
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

# 상하좌우
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 최대값
max_value = 0

# dfs로 탐색 가능한 모양들
def dfs(i, j, dsum, cnt):
    global max_value
    if cnt == 4:
        max_value = max(max_value, dsum)
        return
    
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False

# dfs로 탐색 불가능한 ㅗ, ㅜ, ㅓ, ㅏ 모양들
def exception(i, j):
    global max_value
    for n in range(4):
        tmp = board[i][j]
        for k in range(3):
            t = (n + k) % 4
            # move 배열의 요소를 3개씩 사용하도록 하는 for문
            # 3개씩 사용하되 한칸씩 밀어서 다른 3개를 사용하도록 t 설정
            ni = i+move[t][0]
            nj = j+move[t][1]
            
            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
            
        max_value = max(max_value, tmp)
        
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exception(i, j )

print(max_value)