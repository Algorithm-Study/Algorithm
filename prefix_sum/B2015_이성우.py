from collections import defaultdict
N, K = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

pre_sum = [0]*N
pre_dict = defaultdict(int)

pre_dict[0] = 1

for i in range(N):
    pre_sum[i] = pre_sum[i-1] + arr[i]
    if pre_dict[pre_sum[i] - K] > 0:
        answer += pre_dict[pre_sum[i] - K]
    pre_dict[pre_sum[i]] += 1

print(answer)
