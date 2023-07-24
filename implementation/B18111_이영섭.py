import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = float('inf')
idx = 0

for floor in range(257):
    max_target, min_target = 0, 0

    for i in range(N):
        for j in range(M):
            if board[i][j] >= floor:
                max_target += board[i][j] - floor
            else:
                min_target += floor - board[i][j]

    if max_target + H >= min_target:
        if min_target + (max_target * 2) <= ans:
            ans = min_target + (max_target * 2)
            idx = floor

print(ans, idx)
