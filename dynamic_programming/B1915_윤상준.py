n, m = map(int, input().split())
field = [list(map(int, list(input()))) for _ in range(n)]
max_length = 0
for i in range(n):
    for j in range(m):
        if field[i][j] != 0 and i*j != 0:
            field[i][j] += min(field[i][j-1], field[i-1][j], field[i-1][j-1])
        max_length = max(max_length, field[i][j])
print(max_length**2)