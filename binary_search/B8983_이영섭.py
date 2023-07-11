import sys
input = sys.stdin.readline

M, N, L = map(int, input().strip().split())
s_point = sorted(list(map(int, input().strip().split())))
a_point = [list(map(int, input().strip().split())) for _ in range(N)]
ans = 0

for x, y in a_point:
    start, end = 0, len(s_point) - 1
    while start < end:
        mid = (start + end) // 2
        if s_point[mid] < x:
            start = mid + 1
        elif s_point[mid] > x:
            end = mid - 1
        else:
            start = mid
            break
    if abs(s_point[start] - x) + y <= L:
        ans += 1
    elif start + 1 < len(s_point) and abs(s_point[start + 1] - x) + y <= L:
        ans += 1
    elif start > 0 and abs(s_point[start - 1] - x) + y <= L:
        ans += 1
print(ans)