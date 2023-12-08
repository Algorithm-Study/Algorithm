n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort(key = lambda x: x[0])
LIS = [0]*501
for s, d in line:
    LIS[d] = max(LIS[:d])+ 1
print(n- max(LIS))