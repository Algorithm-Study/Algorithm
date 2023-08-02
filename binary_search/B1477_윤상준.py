n,m,l = list(map(int, input().split()))
stations = [0] + list(map(int, input().split())) + [l]
stations.sort()
start, end = 1, l-1
while start <= end:
    count = 0
    mid = (start + end)//2
    for i in range(1, n+2):
        if stations[i] - stations[i-1] > mid:
            count += (stations[i] - stations[i-1] - 1)//mid
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
print(start)

# 휴게소 간 거리에 대해 이분탐색을 진행하면 됨