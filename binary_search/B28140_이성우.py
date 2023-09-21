import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()
r_idx = []
b_idx = []

for i in range(n):
    if s[i] == 'R':
        r_idx.append(i)
    elif s[i] == 'B':
        b_idx.append(i)

for _ in range(q):
    a = b = c = d = -1
    l, r = map(int, input().split())
    
    if not r_idx or not b_idx:
        print(-1)
        continue
    
    a_idx = bisect_left(r_idx, l)
    a = r_idx[a_idx] if 0 <= a_idx < len(r_idx) else -1

    if a_idx + 1 < len(r_idx):
        b = r_idx[a_idx + 1]

    d_idx = bisect_right(b_idx, r) - 1
    d = b_idx[d_idx] if 0 <= d_idx < len(b_idx) else -1
    
    if d_idx > 0:
        c = b_idx[d_idx - 1]
    
    print(a,b,c,d) if a < b < c < d else print(-1)
        