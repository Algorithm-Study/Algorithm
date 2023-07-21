import sys
n, m, b = map(int,input().split())
block = [list(map(int, input().split())) for _ in range(n)]
time = sys.maxsize
height = 0
for i in range(257):
    inventory, get = 0, 0
    for j in range(n):
        for k in range(m):
            if block[j][k] > i:
                get += block[j][k] - i
            else:
                inventory += i - block[j][k]
    if inventory > get + b:
        continue
    c_time = get * 2 + inventory
    if c_time <= time:
        time = c_time
        height = i

print(time, height)
# 각 높이 별 소요시간을 구해서 갱신하는 문제
# 인벤토리에 더이상 흙이 없는 경우 고려해야 함