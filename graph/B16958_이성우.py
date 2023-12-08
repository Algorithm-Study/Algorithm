import sys
from itertools import combinations
input = sys.stdin.readline
INF = sys.maxsize

n, t = map(int, input().split())
arr = [[INF]*(n+1) for _ in range(n+1)]
city = []

for idx in range(1, n+1):
    s, x, y = map(int, input().split())
    city.append((idx, s, x, y))
    
for case in combinations(city, 2):
    c1, c2 = case
    if c1[1] == 1 and c2[1] == 1:
        arr[c1[0]][c2[0]] = min(abs(c1[2]-c2[2]) + abs(c1[3]-c2[3]), t)
        arr[c2[0]][c1[0]] = min(abs(c1[2]-c2[2]) + abs(c1[3]-c2[3]), t)
    else:
        arr[c1[0]][c2[0]] = abs(c1[2]-c2[2]) + abs(c1[3]-c2[3])
        arr[c2[0]][c1[0]] = abs(c1[2]-c2[2]) + abs(c1[3]-c2[3])
        
for k in range(1, n+1):
    arr[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                
for _ in range(int(input().rstrip())):
    a, b = map(int, input().split())
    print(arr[a][b])