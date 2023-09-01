import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
light = list(map(int, input().split()))
new_list = [light[0]]

for i in range(1, N):
    if new_list[-1] < light[i]:
        new_list.append(light[i])
    else:
        tp = bisect_left(new_list, light[i])
        new_list[tp] = light[i]

print(N - len(new_list))
