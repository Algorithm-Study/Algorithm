def solution(m, n, puddles):
    arr = [[0 for j in range(m)]  for i in range(n)]
        
    for i in range(n):
        for j in range(m):
            if i == j == 0:
                arr[i][j] = 1
            elif i == 0 and [j+1,i+1] not in puddles:
                arr[i][j] = arr[i][j-1]%1_000_000_007
            elif j == 0 and [j+1,i+1] not in puddles:
                arr[i][j] = arr[i-1][j]%1_000_000_007
            elif [j+1,i+1] not in puddles:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1])%1_000_000_007

    return arr[n-1][m-1]