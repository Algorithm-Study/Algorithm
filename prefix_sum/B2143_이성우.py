from collections import defaultdict

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

ans = 0
A_dict = defaultdict(int)
tmp = 0
for i in range(n):
    for j in range(i, n):
        tmp += A[j]
        A_dict[tmp] += 1
    tmp = 0

tmp = 0
for i in range(m):
    for j in range(i, m):
        tmp += B[j]
        ans += A_dict[T - tmp]
    tmp = 0

print(ans)