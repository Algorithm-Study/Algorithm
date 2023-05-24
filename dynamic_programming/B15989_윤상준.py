t = int(input())
cases = [1]*10_001
for i in range(2,10001):
    cases[i] += cases[i-2]
for i in range(3,10001):
    cases[i] += cases[i-3]
for _ in range(t):
    num = int(input())
    print(cases[num])
# 순서가 바뀐 경우가 같기 때문에 2차원 dp가 아니라 일차원 dp로 진행해야 함