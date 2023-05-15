maps = [list(map(int, list(input().rstrip()))) for _ in range(9)]
# for _ in maps:
#     print(*_)

zeros = [(i, j) for i in range(9) for j in range(9) if not maps[i][j]]
nums = [i for i in range(1,10)]

def dfs(n):
    if n == len(zeros):
        for i in maps:
            print(*i,sep='')
        exit()

    x, y = zeros[n]
    a, b = x//3, y//3
    tmp = nums[:]

    for i in range(3*a, (a+1)*3):
        for j in range(3*b, (b+1)*3):
            if maps[i][j] in tmp:
                tmp.remove(maps[i][j])

    for i in range(9):
        if maps[x][i] in tmp:
            tmp.remove(maps[x][i])
        if maps[i][y] in tmp:
            tmp.remove(maps[i][y])

    for i in tmp:
        maps[x][y] = i
        dfs(n+1)
    maps[x][y] = 0
    
dfs(0)