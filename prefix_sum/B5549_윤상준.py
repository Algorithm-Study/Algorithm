import sys
input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())
field = [list(input()) for _ in range(n)]
jsum = [[0]*(m+1) for _ in range(n+1)]
osum = [[0]*(m+1) for _ in range(n+1)]
isum = [[0]*(m+1) for _ in range(n+1)]
# 누적합 구하기
for i in range(1,n + 1):
    for j in range(1, m + 1):
        if field[i-1][j-1] == 'J':
            jsum[i][j] = jsum[i][j] + 1
        elif field[i-1][j-1] == 'O':
            osum[i][j] = osum[i][j] + 1
        else:
            isum[i][j] = isum[i][j] + 1
        jsum[i][j] = jsum[i][j-1] + jsum[i-1][j] - jsum[i-1][j-1] + jsum[i][j]
        osum[i][j] = osum[i][j-1] + osum[i-1][j] - osum[i-1][j-1] + osum[i][j]
        isum[i][j] = isum[i][j-1] + isum[i-1][j] - isum[i-1][j-1] + isum[i][j]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    jungle = jsum[x2][y2] - jsum[x2][y1-1] - jsum[x1-1][y2] + jsum[x1-1][y1-1]
    ocean = osum[x2][y2] - osum[x2][y1-1] - osum[x1-1][y2] + osum[x1-1][y1-1]
    ice = isum[x2][y2] - isum[x2][y1-1] - isum[x1-1][y2] + isum[x1-1][y1-1]
    print(jungle, ocean, ice)