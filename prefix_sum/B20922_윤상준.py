from collections import deque
from collections import defaultdict
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
counter = defaultdict(int)
subsequence = deque()
max_len = 0
for s in sequence:
    subsequence.append(s)
    counter[s] += 1
    if counter[s] <= k:
        max_len = max(max_len, len(subsequence))
    else:
        while counter[s] > k:
            temp = subsequence.popleft()
            counter[temp] -= 1
print(max_len)
# 덱으로 투포인터처럼 문제 풀이 가능