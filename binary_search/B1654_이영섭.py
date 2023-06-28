import sys
input = sys.stdin.readline

K, N = map(int, input().split())
data = [int(input()) for _ in range(K)]
left, right, ans = 1, max(data), 1

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for d in data:
        cnt += d // mid
    if cnt >= N:
        ans = max(mid, ans)
        left = mid + 1
    else:
        right = mid - 1
print(ans)