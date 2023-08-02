import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [],[],[],[]
total = 0
value = {}
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
for i in range(n):
    for j in range(n):
        value.setdefault(A[i] + B[j], 0)
        value[A[i] + B[j]] += 1
for i in range(n):
    for j in range(n):
            total += value.get(-C[i]-D[j], 0)
print(total)

# 두 개 씩 짝을 나눠서 반대 값이 존재하는지 확인하는 문제
# python에게는 시간이 빡빡함