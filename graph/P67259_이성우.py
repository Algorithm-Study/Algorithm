from collections import deque

def solution(board):
    result = float('inf')
    N = len(board)
    direction = [[0, 1, 0], [1, 0, 1], [0, -1, 2], [-1, 0, 3]]
    dp = [[[10000] * N for i in range(N)] for j in range(4)]
    queue = deque()
    queue.append([0, 0, 0, 0])
    queue.append([0, 0, 0, 1])
    
    while queue:
        x, y, m, d = queue.popleft()
        
        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                nm= m + 1
                if d != direction[i][2]:
                    nm += 5
                if nm < dp[direction[i][2]][nx][ny]:
                    dp[direction[i][2]][nx][ny] = nm
                    if nx == N-1 and ny == N-1:
                        continue
                    queue.append([nx, ny, nm, direction[i][2]])
    for i in range(4):
        result = min([result, dp[i][N-1][N-1]])
    return result * 100