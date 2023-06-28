N, S = map(int, input().split())
suyeol = list(map(int, input().split()))
left, right, sum, min_len = 0, 0, suyeol[0], 100001
while left <= right:
    if sum >= S:
        sum -= suyeol[left]
        min_len = min(min_len, right - left + 1)
        left += 1
    else:
        right += 1
        if right == N:
            break
        sum += suyeol[right]
if min_len == 100001:
    print(0)
else:
    print(min_len)