import sys
from collections import deque
input = sys.stdin.readline

l = int(input())
ml, mk = map(int, input().split())
c = int(input())
arr = [0] + [int(input()) for _ in range(l)]

# 쌓인 데미지 계산
prefix_sum = [0]

for idx in range(1, l+1):
    out_of_range = max(0, idx-ml)
    damage = prefix_sum[idx-1] - prefix_sum[out_of_range]
    
    if arr[idx] <= damage + mk:
        prefix_sum.append(prefix_sum[idx-1] + mk)
    else:
        if c > 0:
            c -= 1
            prefix_sum.append(prefix_sum[idx-1])
        else:
            print('NO')
            break
else:
    print('YES')