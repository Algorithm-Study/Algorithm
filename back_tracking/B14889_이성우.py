import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]
members = list(range(n))
min_val = float('inf')

for r1 in combinations(members, n//2):
    start, link = 0, 0
    r2 = list(set(members) - set(r1))
    for r in combinations(r1, 2):
        start += arr[r[0]][r[1]]
        start += arr[r[1]][r[0]]
    for r in combinations(r2, 2):
        link += arr[r[0]][r[1]]
        link += arr[r[1]][r[0]]
    min_val = min(min_val, abs(start-link))
print(min_val)