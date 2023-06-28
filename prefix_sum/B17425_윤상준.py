import sys
input = sys.stdin.readline
prefix = [1]* 1_000_001
prefix[0] = 0
for i in range(2,1_000_001):
    for j in range(1,1_000_000//i + 1):
        prefix[i*j] += i
    prefix[i] += prefix[i-1]
t = int(input())
for _ in range(t):
    n = int(input())
    print(prefix[n])

# 각 값들의 약수의 합 f(A)를 구한 다음 누적합으로 변경
# 이후 입력에 맞는 위치의 값을 출력하면 끝
# 누적합 계산 전에 입력을 받으면 시간초과 발생