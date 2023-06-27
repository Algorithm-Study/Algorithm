n, tc = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tc = [list(map(int, input().split())) for _ in range(tc)]

sum_arr = [[0 for _ in range(n+1)] for _ in range(n)]

for i in range(n):
    for j in range(1,n+1):
        sum_arr[i][j] = sum_arr[i][j-1] + arr[i][j-1]
        
for x1, y1, x2, y2 in tc:
    answer = 0
    for r in range(x1, x2+1):
        answer += sum_arr[r-1][y2] - sum_arr[r-1][y1-1]

    print(answer)