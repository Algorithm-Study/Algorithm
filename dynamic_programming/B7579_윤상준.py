n, m = map(int, input().split())
activate = list(map(int, input().split()))
deactivate = list(map(int, input().split()))
max_val = sum(deactivate) + 1
backpack = [[0 for _ in range(max_val)] for _ in range(n+1)]
result = max_val
for i in range(n):
    for j in range(max_val):
        if deactivate[i] > j:
            backpack[i][j] = backpack[i-1][j]
        else:
            backpack[i][j] = max(backpack[i-1][j], activate[i] + backpack[i-1][j - deactivate[i]])
        
        if backpack[i][j] >= m:
            result = min(result, j)
if m == 0:
    print(0)
else:
    print(result)