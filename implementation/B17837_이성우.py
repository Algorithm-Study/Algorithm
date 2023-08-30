# 4:34
# n*n 체스판
n, k = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(n)]
arr = [[[] for _ in range(n)] for _ in range(n)]
horse = []

class Horse():
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dr = [1, 0, 3, 2]

for i in range(k):
    x, y, d = map(int, input().split())
    arr[x-1][y-1].append(i)
    horse.append(Horse(x-1, y-1, d-1))

def pick(h):
    tmp = []
    idx = arr[horse[h].x][horse[h].y].index(h)
    for _ in range(len(arr[horse[h].x][horse[h].y])-idx):
        tmp.append(arr[horse[h].x][horse[h].y].pop())
    return tmp[::-1]
    
def move(h, tmp, cnt):
    nx = horse[h].x + dx[horse[h].d]
    ny = horse[h].y + dy[horse[h].d]

    if 0 <= nx < n and 0 <= ny < n:
        if color[nx][ny] == 0:
            arr[nx][ny].extend(tmp)
            for i in tmp:
                horse[i].x = nx
                horse[i].y = ny
        elif color[nx][ny] == 1:
            arr[nx][ny].extend(tmp[::-1])
            for i in tmp:
                horse[i].x = nx
                horse[i].y = ny
        else:
            if cnt == 0:
                horse[h].d = dr[horse[h].d]
                move(h, tmp, 1)
            else:
                arr[horse[h].x][horse[h].y].extend(tmp)
    else:
        if cnt == 0:
            horse[h].d = dr[horse[h].d]
            move(h, tmp, 1)
        else:
            arr[horse[h].x][horse[h].y].extend(tmp)
    
# 턴한번은 1~k번까지 순서대로이동
# 한 말이 이동할 때 위에 올려져 있는 말도 이동
# 이동 방향은 정해져 있다
# 말이 4개 이상 쌓이면 종료

# 이동하는 칸이 흰색이면 그 칸으로 이동하고 말이 있다면 그 말위에 올려놓는다

# 이동하는 칸이 빨간색이면 그 칸으로 이동하고 말이 있다면 그 말위에 놓으려는 말을 뒤집어서 올린다

# 파란색인 경우 이동 방향을 반대로 하고 한 칸 이동
# 반대로 방향을 바꾼 후 이동하려는 칸이 파란색이면 이동하지 않고 가만히 있는다

# 체스판을 벗어나면 파란색과 같다

answer = 1
while 1001 - answer:
    for i in range(k):
        tmp = pick(i)
        move(i, tmp, 0)
        for h in range(k):
            if len(arr[horse[h].x][horse[h].y]) >= 4:
                print(answer)
                exit()    
    answer += 1
print(-1)

# 100분 요소
# x, y 변수 오타 실수

# 놓친 조건
# 말위의 말들 위치 갱신
# 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.