class Player:
    def __init__(self, x, y, d, s, idx):
        self.x = x-1
        self.y = y-1
        self.d = d
        self.s = s
        self.g = 0
        self.a = self.s + self.g
        self.p = 0
        self.idx = idx
        
# 첫번째 플레이어부터 본인이 향하는 방향대로 한 칸 이동한다
# 격자를 나가면 반대로 1칸 이동            
    def move(self):
        nx = self.x + dx[self.d]
        ny = self.y + dy[self.d]
        if 0 <= nx < n and 0 <= ny < n:
            self.x = nx
            self.y = ny
        else:
            self.x = self.x - dx[self.d]
            self.y = self.y - dy[self.d]
            self.d = dr[self.d]
    
# 이동한 방향에 플레이어가 없고 총이 있다면 더 강력한 총으로 교환
# 남은 총은 격자에 내려둔다
    def get_gun(self):
        candi = max(arr[self.x][self.y])
        if self.g < candi:
            arr[self.x][self.y].remove(candi)
            arr[self.x][self.y].append(self.g)
            self.g = candi
        self.a = self.s + self.g
            
    def win(self):
        self.get_gun()
        
    def lose(self):
        arr[self.x][self.y].append(self.g)
        self.g = 0
        for i in range(4):
            nd = (self.d+i) % 4
            nx = self.x + dx[nd]
            ny = self.y + dy[nd]
            crash = False
            if 0 <= nx < n and 0 <= ny < n:
                for j in range(m):
                    if self.idx != j and nx == player[j].x and ny == player[j].y:
                        crash = True
                        break
                if crash:
                    continue
                self.x = nx
                self.y = ny
                self.d = nd
                break
        self.get_gun()
# 이동한방향에 플레이어가 있다면 전투
# 초기 능력과 총 공격력의 합으로 비교하여 승리

# 수치가 같다면 초기 능력이 같은 사람이 이김
# 이긴 플레이어는 총 공격력의 차이만큼 포인트 획득

# 진 플레이어는 총을 내려놓고 원래 방향으로 한칸 이동
# 이동할 수 없다면 오른쪽으로 90도씩 회전하여 빈칸이 있는 곳으로 이동
# 총이 있다면 가장 강력한 총 획득

# 이긴 플레이어는 승리한 칸에 떨어져 있는 총들중 가장 강력한 총을 갖고
# 남은 총은 격자에 내려놓음
def battle(p1, p2):
    if p1.a > p2.a:
        p1.p += p1.a - p2.a
        winner = p1
        loser = p2
    elif p1.a < p2.a:
        p2.p += p2.a - p1.a
        winner = p2
        loser = p1
    else:
        if p1.s > p2.s:
            winner = p1
            loser = p2
        else:
            winner = p2
            loser = p1
    loser.lose()
    winner.win()
    
# 초기값 설정
n, m, k = map(int, input().split())

tmp = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dr = [2, 3, 0, 1]

arr = [[[] for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j].append(tmp[i][j])

# 각 격자에는 무기가 있고 무기가 없는 빈 격자에는 플레이어가 있다
# 플레이어는 각기 다른 초기 능력치를 가진다
# 배경은 총의 공격력을 나타낸다
player = []
for i in range(m):
    x, y, d, s = map(int, input().split())
    p = Player(x, y, d, s, i)
    player.append(p)
    
for _ in range(k):
    for i in range(m):
        player[i].move()
        for j in range(m):
            if i != j and player[i].x == player[j].x and player[i].y == player[j].y:
                battle(player[i], player[j])
                break
        else:
            player[i].get_gun()

for i in range(m):
    print(player[i].p, end=' ')

# 방향 갱신 안해준거, 지고 나서 플레이어 있는 곳은 못가는거
# 벽을 향할 때 방향 갱신 잘못해준거...