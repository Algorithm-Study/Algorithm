from collections import Counter

T = int(input())
for _ in range(T):
    W = input()
    K = int(input())
    min_ans, max_ans = float('inf'), 0
    str_dict = Counter(W)
    for key, val in str_dict.items():
        if val < K:
            continue
        index = [i for i, c in enumerate(W) if c == key]
        idx_val = [index[i+K-1] - index[i] + 1 for i in range(len(index) + 1 - K)]
        if min(idx_val) < min_ans:
            min_ans = min(idx_val)
        if max(idx_val) > max_ans:
            max_ans = max(idx_val)
    if min_ans == float('inf') and max_ans == 0:
        print(-1)
    else:
        print(min_ans, max_ans)
