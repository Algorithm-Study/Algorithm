import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
tmp = [arr[0]]

for i in range(1, n):
    if arr[i] > tmp[-1]:
        tmp.append(arr[i])
    else:
        idx = bisect_left(tmp, arr[i])
        tmp[idx] = arr[i]
        
print(n - len(tmp))

