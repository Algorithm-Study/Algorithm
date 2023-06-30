n, c = map(int, input().split())
data = []
for i in range(n):
    data.append(int(input()))
data.sort()
start = 1
end = data[-1] - data[0]
result = 0
while start <=end:
    mid = (start + end)//2
    value = data[0]
    count = 1
    for i in range(1,n):
        if data[i] >= value + mid:
            value = data[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
# 최대 거리를 구해야 하므로 거리에 대한 이분 탐색을 진행하면 됨