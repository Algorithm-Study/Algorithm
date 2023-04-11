# 순차적으로 최솟값을 구해야 함
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
cost = [[0 for _ in range(n)] for _ in range(n)]
   
for i in range(1,n): #열 먼저
    for j in range(n-i):
        if i == 1:
            cost[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue
        cost[j][j + i] = 2**31
        for k in range(j, j+i):
            cost[j][j+i] = min(cost[j][j+i], cost[j][k] + cost[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
print(cost[0][n-1])