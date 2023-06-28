import sys
input = sys.stdin.readline

N, C = map(int, input().split())
data, ans = [], 0
for _ in range(N):
    data.append(int(input()))
data.sort()

left, right = 1, data[-1] - data[0]
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    last = data[0]
    for i in range(1, N):
        if data[i] - last >= mid:
            cnt += 1
            last = data[i]
    if cnt >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)