import copy

def move_monster():
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(8):
                    nd = (d + i)%8
                    nx, ny = x + p_dx[nd], y + p_dy[nd]
                    if (nx, ny) != pack and 0 <= nx < 4 and 0 <= ny < 4 and not ghost[nx][ny]:
                        res[nx][ny].append(nd)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    global max_eat, pack, eat
    if dep == 3:   # 3번 이동한 경우 그만 
        if max_eat < cnt:
            max_eat = cnt
            pack = (x, y)
            eat = visit[:]

        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if (nx, ny) not in visit:
                visit.append((nx, ny))
                dfs(nx, ny, dep + 1, cnt + len(temp[nx][ny]), visit)
                visit.pop()
            else:  # 방문한 경우
                dfs(nx, ny, dep + 1, cnt, visit)

p_dx = [-1, -1, 0, 1, 1, 1, 0, -1]
p_dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, t = map(int, input().split())
r, c = map(int, input().split())
arr = [[[] for _ in range(4)] for _ in range(4)]
pack = (r-1, c-1)
for _ in range(m):
    x, y, d = map(int, input().split())
    arr[x-1][y-1].append(d-1)

ghost = [[0] * 4 for _ in range(4)]

for _ in range(t):
    eat = []
    max_eat = -1
    # 1. 모든 몬스터 복제
    temp = copy.deepcopy(arr)
    # 2. 몬스터 이동
    temp = move_monster()

    # 3. 팩맨이동 - 백트래킹
    dfs(pack[0], pack[1], 0, 0, [])
    for x, y in eat:
        if temp[x][y]:
            temp[x][y] = []
            ghost[x][y] = 3   # 3번 돌아야 없어짐
    # 4. 유령 사라짐 
    for i in range(4):
        for j in range(4):
            if ghost[i][j]:
                ghost[i][j] -= 1
    # 5. 복제
    for i in range(4):
        for j in range(4):
            arr[i][j] += temp[i][j]

# 몬스터 수 구하기 
answer = 0
for i in range(4):
    for j in range(4):
        answer += len(arr[i][j])

print(answer)