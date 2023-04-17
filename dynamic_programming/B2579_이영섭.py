n = int(input())
data = [int(input()) for _ in range(n)]

score = [[0]*2 for _ in range(n)]
# 0이 두 계단, 1이 바로 전 계단
if n == 1:
    print(data[0])
elif n == 2:
    print(data[0] + data[1])
else:
    score[0][0], score[0][1] = data[0], data[0]
    score[1][0], score[1][1] = data[1], data[0]+data[1]
    for i in range(2, n):
        score[i][0] = max(score[i-2][0], score[i-2][1]) + data[i]
        score[i][1] = score[i-1][0] + data[i]
    print(max(score[-1]))
