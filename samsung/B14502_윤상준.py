import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lab = []
temp = [[0] *m for _ in range(n)]
for i in range(n):
    lab.append(list(map(int, input().split())))
#print(lab)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0


def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                dfs(count)
                lab[i][j] = 0
                count -= 1


dfs(0)
print(result)
