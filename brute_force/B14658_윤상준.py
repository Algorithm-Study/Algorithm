# 시간 및 메모리가 타이트한 문제
import sys
input = sys.stdin.readline
N, M, L, K = map(int, input().split())
stardust = []
for _ in range(K):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    stardust.append([y, x])
rebound = 0
for x, y in stardust:
    for x2, y2 in stardust:
        bound = 0
        for nx, ny in stardust:
            if x <= nx <= x+L and y2 <= ny <= y2+L:
                bound += 1
        rebound = max(rebound, bound)

print(K - rebound)