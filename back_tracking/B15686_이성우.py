from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = float('inf')
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

for com in combinations(chicken, m):
    tmp = 0
    for h in house:
        tmp += min([abs(h[0]-c[0]) + abs(h[1]-c[1]) for c in com])
    answer = min(answer, tmp)
    
print(answer)