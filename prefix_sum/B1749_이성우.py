import sys
input =sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + arr[i-1][j-1] - prefix_sum[i-1][j-1]
        
answer = float('-inf')

for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1 , m+1):
                answer = max(answer, prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])

print(answer)