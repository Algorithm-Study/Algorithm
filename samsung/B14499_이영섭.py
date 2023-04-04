dice = [0, 0, 0, 0, 0, 0]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
comm = list(map(int, input().split()))

def move_dice(num): # 동,서,북,남,위,아래
    global dice
    if num == 1: # 위,아래,북,남,서,동
        temp = [dice[4], dice[5], dice[2], dice[3], dice[1], dice[0]]
    elif num == 2: # 아래,위,북,남,동,서
        temp = [dice[5], dice[4], dice[2], dice[3], dice[0], dice[1]]
    elif num == 3: # 동,서,아래,위,남,북
        temp = [dice[0], dice[1], dice[4], dice[5], dice[3], dice[2]]
    else: # 동,서,위,아래,북,남
        temp = [dice[0], dice[1], dice[5], dice[4], dice[2], dice[3]]
    dice = temp

for com in comm:
    nx = x + dx[com-1]
    ny = y + dy[com-1]
    if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
    x += dx[com-1]
    y += dy[com-1]
    move_dice(com)
    if board[x][y] == 0: board[x][y] = dice[5]
    else: 
        dice[5] = board[x][y]
        board[x][y] = 0
    print(dice[4])
    
# 문제 접근 방법
# # 주사위와 주사위 움직임을 구현하는 함수를 만들고 명령에 따라 함수를 반복 실행