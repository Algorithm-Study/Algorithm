from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
S = list(input())
r_list, b_list = [], []

for i in range(N):
    if S[i] == 'R':
        r_list.append(i)
    elif S[i] == 'B':
        b_list.append(i)

for _ in range(Q):
    l, r = map(int, input().split())
    r1 = bisect_left(r_list, l)
    r2 = bisect_right(r_list, r)
    b1 = bisect_left(b_list, l)
    b2 = bisect_right(b_list, r)
    r2 -= 1
    b2 -= 1
    if r2 - r1 + 1 < 2 or b2 - b1 + 1 < 2:
        print(-1)
        continue
    if r_list[r1 + 1] >= b_list[b2 - 1]:
        print(-1)
        continue
    print(r_list[r1], r_list[r1 + 1], b_list[b2 - 1], b_list[b2])
