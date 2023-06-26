import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = []
s_data = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    data.append(list(map(int, input().split())))
    for j in range(n):
        s_data[i+1][j+1] = s_data[i][j+1] + s_data[i+1][j] - s_data[i][j] + data[i][j]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = s_data[x2][y2] - s_data[x1-1][y2] - s_data[x2][y1-1] + s_data[x1-1][y1-1]
    print(total)
# dp로 누적합 구한 다음에 관계에 따라 계산해주면 풀리는 문제