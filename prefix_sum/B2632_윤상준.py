from collections import defaultdict
size = int(input())
p1,p2 = [], []
n,m = map(int, input().split())
for _ in range(n):
    p1.append(int(input()))
for _ in range(m):
    p2.append(int(input()))
pizza1, pizza2 = defaultdict(int), defaultdict(int)
pizza1[0], pizza2[0] = 1, 1
pizza1[sum(p1)], pizza2[sum(p2)] = 1, 1
# 각 조각별 가능한 경우 찾기
for i in range(n):
    total = p1[i]
    pizza1[total] += 1
    for j in range(1,n-1):
        total += p1[(i+j)%n]
        pizza1[total] += 1
for i in range(m):
    total = p2[i]
    pizza2[total] += 1
    for j in range(1,m-1):
        total += p2[(i+j)%m]
        pizza2[total] += 1
result = 0
# 선택한 조각에 대해서 조건을 충족하는지 확인
for i in range(size+1):
    result += pizza1[i]*pizza2[size-i]
print(result)