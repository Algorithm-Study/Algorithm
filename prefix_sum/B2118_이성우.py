n = int(input())
distance = [int(input()) for _ in range(n)]

prefix_sum = [0]*(n*2+1)
for i in range(n*2):
    prefix_sum[i+1] = prefix_sum[i] + distance[i%n]
    
answer = 0
sum_ = sum(distance)
right = 1
for left in range(n*2):
    # 시계 방향 거리가 반시계 방향 거리보다 크면 거리를 줄인다
    while right < n*2 + 1 and prefix_sum[right] - prefix_sum[left] <= sum_ - (prefix_sum[right] - prefix_sum[left]):
        answer = max(answer, prefix_sum[right]-prefix_sum[left])
        right += 1
print(answer)