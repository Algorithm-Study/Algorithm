n, E, W, S, N = map(int, input().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
percent = [E/100, W/100, S/100, N/100]
ans = 0


def dfs(x, y, per, cnt, visit):
    global ans
    if cnt == n:
        ans += per
        return
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if (nx, ny) not in visit:
            visit.append((nx, ny))
            dfs(nx, ny, per*percent[di], cnt + 1, visit)
            visit.pop()


dfs(0, 0, 1, 0, [(0, 0)])
print(ans)