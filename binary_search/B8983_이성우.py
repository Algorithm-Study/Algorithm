import sys
from bisect import bisect_left
input = sys.stdin.readline

M, N, L = map(int, input().split())
guns = list(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(N)]
answer = 0

guns.sort()

for _ in range(N):
    x, y = map(int, input().split())
    if y <= L:
        idx = bisect_left(guns, x)
        for k in [idx-1, idx, idx+1]:
            if k < 0 or k >= M:
                continue
            if abs(guns[k] - x) + y <= L:
                answer += 1
                break
print(answer)