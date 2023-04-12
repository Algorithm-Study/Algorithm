INF = 1e8
command = list(map(int, input().split()))
if len(command) == 1:
    print(0)
else:
    foot = [[[INF] * 5 for _ in range(5)] for _ in range(len(command) - 1)]
    foot[0][command[0]][0] = 2
    foot[0][0][command[0]] = 2
    for i in range(1, len(command)-1):
        togo = command[i]
        for j in range(5):
            # print(i, j)
            val = foot[i][togo][j]
            for k in range(5):
                if k == togo and k != 0:
                    val = min(val, foot[i-1][k][j] + 1)
                elif k == 0 or togo == 0:
                    val = min(val, foot[i-1][k][j] + 2)
                elif abs(k - togo) == 1 or abs(k - togo) == 3:
                    val = min(val, foot[i-1][k][j] + 3)
                elif abs(k - togo) == 2:
                    val = min(val, foot[i-1][k][j] + 4)
            foot[i][togo][j] = val
        for j in range(5):
            val = foot[i][j][togo]
            for k in range(5):
                if k == togo and k != 0:
                    val = min(val, foot[i-1][j][k] + 1)
                elif k == 0 or togo == 0:
                    val = min(val, foot[i-1][j][k] + 2)
                elif abs(k - togo) == 1 or abs(k - togo) == 3:
                    val = min(val, foot[i-1][j][k] + 3)
                elif abs(k - togo) == 2:
                    val = min(val, foot[i-1][j][k] + 4)
            foot[i][j][togo] = val
    ans = INF
    # for i in range(len(foot)):
    #     for j in range(5):
    #         print(foot[i][j])
    #     print()
    for i in range(len(foot[-1])):
        temp = min(foot[-1][i])
        ans = min(ans, temp)
    print(ans)
    
# 문제 접근 방법
# # foot[i][j][k]를 i번째 왼발(j), 오른발(k) 위치의 최솟값을 구한다고 생각