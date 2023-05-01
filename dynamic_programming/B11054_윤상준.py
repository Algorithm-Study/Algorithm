n = int(input())
sequence = list(map(int, input().split()))
r_sequence = sequence[::-1]
LIS = [1]*n
LDS = [1]*n
for i in range(n):
    for j in range(i):
        if sequence[i] > sequence[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)
        if r_sequence[i] > r_sequence[j]:
            LDS[i] = max(LDS[i], LDS[j] + 1)
result = [LIS[x] + LDS[n-x-1] -1 for x in range(n)]
print(max(result))
# 한번에 처리하는 것이 아니라 양방향으로 LCS 계산 후 최대 길이가 되는 경우를 찾으면 문제 해결 가능