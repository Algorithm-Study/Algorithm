ways = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
n,m,k = map(int, input().split())
field = [[0]+[5]*n for _ in range(n+1)]
trees = [[[] for _ in range(n+1)] for _ in range(n+1)]
energy = [[0]*(n+1)]
for _ in range(n):
    line = [0] + list(map(int, input().split()))
    energy.append(line)
for _ in range(m):
    r,c, age = map(int, input().split())
    trees[r][c].append(age)
for _ in range(k):
    #봄
    death = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            renew = []
            for tree in sorted(trees[i][j]):
                # 양분이 트리보다 많은 경우(성장)
                if field[i][j] >= tree:
                    renew.append(tree + 1)
                    field[i][j] -= tree
                # 죽었으므로 양분으로 추가
                else:
                    death[i][j] += tree//2
            trees[i][j] = renew
    #여름
    for i in range(1,n+1):
        for j in range(1,n+1):
            field[i][j] += death[i][j]
    #가을
    for i in range(1,n+1):
        for j in range(1,n+1):
            for tree in sorted(trees[i][j]):
                # 번식 대상 나무
                if tree % 5 == 0:
                    x, y = i, j
                    for way in ways:
                        nx = x + way[0]
                        ny = y + way[1]
                        if nx < 1 or ny < 1 or nx >= n+1 or ny >= n+1:
                            continue
                        trees[nx][ny].append(1)
    #겨울
    for i in range(1,n+1):
        for j in range(1,n+1):
            field[i][j] += energy[i][j]
total = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        total += len(trees[i][j])
print(total)

# 범위에 주의할 것