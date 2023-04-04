def check(sand, x, y, per, key=None):
    global ans
    # print(x, y)
    if key != None:
        if x < 0 or x >= N or y < 0 or y >= N:
            ans += sand
            return 0
        else:
            board[x][y] += sand
            return 0
    val = sand * per //100
    if x < 0 or x >= N or y < 0 or y >= N:
        ans += val
        return val
    else: 
        board[x][y] += val
        return val

def move_sand(x, y, num):
    sand = board[x][y]
    left_sand = 0
    if num == 1:
        left_sand += check(sand, x-2, y, 2)
        left_sand += check(sand, x-1, y-1, 10)
        left_sand += check(sand, x-1, y, 7)
        left_sand += check(sand, x-1, y+1, 1)
        left_sand += check(sand, x, y-2, 5)
        left_sand += check(sand, x+1, y-1, 10)
        left_sand += check(sand, x+1, y, 7)
        left_sand += check(sand, x+1, y+1, 1)
        left_sand += check(sand, x+2, y, 2)
        end = check(sand-left_sand, x, y-1, 0, 1)
    elif num == 2:
        left_sand += check(sand, x, y-2, 2)
        left_sand += check(sand, x+1, y-1, 10)
        left_sand += check(sand, x, y-1, 7)
        left_sand += check(sand, x-1, y-1, 1)
        left_sand += check(sand, x+2, y, 5)
        left_sand += check(sand, x+1, y+1, 10)
        left_sand += check(sand, x, y+1, 7)
        left_sand += check(sand, x-1, y+1, 1)
        left_sand += check(sand, x, y+2, 2)
        end = check(sand-left_sand, x+1, y, 0, 1)
    elif num == 3:
        left_sand += check(sand, x-2, y, 2)
        left_sand += check(sand, x-1, y+1, 10)
        left_sand += check(sand, x-1, y, 7)
        left_sand += check(sand, x-1, y-1, 1)
        left_sand += check(sand, x, y+2, 5)
        left_sand += check(sand, x+1, y+1, 10)
        left_sand += check(sand, x+1, y, 7)
        left_sand += check(sand, x+1, y-1, 1)
        left_sand += check(sand, x+2, y, 2)
        end = check(sand-left_sand, x, y+1, 0, 1)
    else:
        left_sand += check(sand, x, y-2, 2)
        left_sand += check(sand, x-1, y-1, 10)
        left_sand += check(sand, x, y-1, 7)
        left_sand += check(sand, x+1, y-1, 1)
        left_sand += check(sand, x-2, y, 5)
        left_sand += check(sand, x-1, y+1, 10)
        left_sand += check(sand, x, y+1, 7)
        left_sand += check(sand, x+1, y+1, 1)
        left_sand += check(sand, x, y+2, 2)
        end = check(sand-left_sand, x-1, y, 0, 1)

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0
x, y = N//2, N//2
for i in range(1, N):
    for j in range(1, 3):
        for _ in range(i):
            num = 0
            if i % 2 == 1 and j == 1:
                x += dx[0]
                y += dy[0]
                num = 1
            elif i % 2 == 1 and j == 2:
                x += dx[1]
                y += dy[1]
                num = 2
            elif i % 2 == 0 and j == 1:
                x += dx[2]
                y += dy[2]
                num = 3
            elif i % 2 == 0 and j == 2:
                x += dx[3]
                y += dy[3]
                num = 4
            # print(x, y, num)
            move_sand(x, y, num)
            # for k in range(len(board)):
            #     print(board[k])

for i in range(N-1):
    x += dx[0]
    y += dy[0]
    move_sand(x, y, 1)

print(ans)

# 문제 접근 방법
# # 배열을 순회하는 for문을 먼저 만들고
# # for 문 안에서 move_sand를 실행하여 모래를 움직이도록 하였다.