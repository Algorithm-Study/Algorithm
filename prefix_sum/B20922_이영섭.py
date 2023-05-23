N, K = map(int, input().split())
data = list(map(int, input().split()))
sum_data = [0] * (max(data) + 1)
left, right = 0, 0
result = 0
while right < N:
    if sum_data[data[right]] < K:
        sum_data[data[right]] += 1
        right += 1
    else:
        sum_data[data[left]] -= 1
        left += 1
    result = max(result, right-left)
print(result)
