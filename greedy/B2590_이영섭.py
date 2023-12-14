paper = [int(input()) for _ in range(6)]

# 6
ans = paper[5]

# 5
while paper[4]:
    ans += 1
    paper[4] -= 1
    if paper[0] > 0:
        paper[0] -= min(11, paper[0])

# 4
while paper[3]:
    p = 20
    ans += 1
    paper[3] -= 1
    if paper[1] > 0:
        p -= min(20, paper[1]*4)
        paper[1] -= min(5, paper[1])
    if paper[0] > 0:
        paper[0] -= min(p, paper[0])

# 3
while paper[2]:
    p = 36
    ans += paper[2] // 4
    paper[2] %= 4
    if paper[2] % 4 == 1:
        ans += 1
        p -= 9
        if paper[1] > 0:
            p -= min(5, paper[1]) * 4
            paper[1] -= min(5, paper[1])
        if paper[0] > 0:
            paper[0] -= min(p, paper[0])
    elif paper[2] % 4 == 2:
        ans += 1
        p -= 18
        if paper[1] > 0:
            p -= min(3, paper[1]) * 4
            paper[1] -= min(3, paper[1])
        if paper[0] > 0:
            paper[0] -= min(p, paper[0])
    elif paper[2] % 4 == 3:
        ans += 1
        p -= 27
        if paper[1] > 0:
            p -= 4
            paper[1] -= 1
        if paper[0] > 0:
            paper[0] -= min(p, paper[0])
    paper[2] = 0

# 2
while paper[1]:
    ans += 1
    p = 36 - min(9, paper[1]) * 4
    paper[1] -= min(9, paper[1])
    if paper[0] > 0:
        paper[0] -= min(p, paper[0])

# 1
while paper[0]:
    ans += 1
    paper[0] -= min(36, paper[0])

print(ans)
