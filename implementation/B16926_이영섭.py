import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def rotate_arr():
    for i in range(min(N, M)//2):
        temp = arr[i][i]
        for row in range(i, M-1-i):
            arr[i][row] = arr[i][row+1]
        for col in range(i, N-1-i):
            arr[col][M-1-i] = arr[col+1][M-1-i]
        for rrow in range(M-1-i, i, -1):
            arr[N-1-i][rrow] = arr[N-1-i][rrow-1]
        for rcol in range(N-1-i, i+1, -1):
            arr[rcol][i] = arr[rcol-1][i]
        arr[i+1][i] = temp

# def rotate_45():
#     new_board = [[0 for _ in range(M)] for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             new_board[i][j] = arr[N - j - 1][i]
#     return new_board

for _ in range(R):
    rotate_arr()
    
for row in arr:
    for val in row:
        print(val, end=" ")
    print()

# 문제 접근 방법
# # Python3로 채점하면 시간 초과이지만 삼성은 pypy3로 채점해주니까 상관없을듯