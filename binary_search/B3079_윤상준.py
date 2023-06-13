import sys
sys.stdin.readline
n, k = map(int, input().split())
waiting = [int(input()) for _ in range(n)]
left, right = min(waiting), max(waiting)*k
result = sys.maxsize
while left <= right:
    passengers = 0
    mid = (left + right)//2
    for i in range(n):
        passengers += mid//waiting[i]
    if passengers >= k:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1
print(result)
# 전체 시간을 찾아야 하기 때문에 전체 시간에 대해 이분탐색 진행