# 1550
from collections import deque
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# > V < ^
# 0 1 2 3

class Dice:
    def __init__(self) -> None:
        self.status = [
                        2,
                    4,  1, 3,
                        5,
                        6
                        ]
        self.d = 0
        self.x = 0
        self.y = 0
        
    
    def forward(self):
        nx = self.x + dx[self.d]
        ny = self.y + dy[self.d]
        if 0 <= nx < n and 0 <= ny < m:
            if self.d == 0:
                self.status = [
                                    self.status[0],
                    self.status[5], self.status[1], self.status[2],
                                    self.status[4],
                                    self.status[3]
                            ]
            elif self.d == 1:
                self.status = [
                                    self.status[5],
                    self.status[1], self.status[0], self.status[3],
                                    self.status[2],
                                    self.status[4]
                            ]
            elif self.d == 2:
                self.status = [
                                    self.status[0],
                    self.status[2], self.status[3], self.status[5],
                                    self.status[4],
                                    self.status[1]
                            ]
            else: # self.d == 3:
                self.status = [
                                    self.status[2],
                    self.status[1], self.status[4], self.status[3],
                                    self.status[5],
                                    self.status[0]
                            ]
            self.x = nx
            self.y = ny
        else:
            self.d = (self.d+2)%4  
            self.forward()
                
    def cw(self):
        self.d = (self.d+1)%4

    def ccw(self):
        self.d = (self.d-1)%4
        

def get_point(i, j):
    num = arr[i][j]
    q = deque()
    visited = [[0]*m for _ in range(n)]
    q.append((i, j))
    visited[i][j] = 1
    p = 1
    
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == num and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                p += 1
    
    return num*p
    
    
dice = Dice()
answer = 0
for _ in range(k):
    dice.forward()
    if dice.status[5] > arr[dice.x][dice.y]:
        dice.cw()
    elif dice.status[5] < arr[dice.x][dice.y]:
        dice.ccw()
    answer += get_point(dice.x, dice.y)
print(answer)

# 1648
# 이동 방향을 회전할 때
# 주사위 자체를 돌리는 줄 알아서 디버깅하는데 시간이 좀 걸렸다