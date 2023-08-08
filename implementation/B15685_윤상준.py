n = int(input())
field = [[0]*101 for _ in range(101)]
ways = [(1,0),(0,-1),(-1,0),(0,1)] # 하 -> 좌 -> 상 -> 우
dragons = [list(map(int, input().split())) for _ in range(n)]
for dragon in dragons:
    x,y,dir,gen = dragon
    field[x][y] = 1
    move = [dir]
    for _ in range(gen):
        temp = []
        for i in range(len(move)):
            temp.append((move[len(move)-i-1] + 1)%4)
        move.extend(temp)
    for m in move:
        nx = x + ways[m][0]
        ny = y + ways[m][1]
        field[nx][ny] = 1
        x, y = nx, ny
result = 0
for i in range(100):
    for j in range(100):
        if sum(field[i][j:j+2]+field[i+1][j:j+2]) == 4:
            print(field[i][j:j+2]+field[i+1][j:j+2])
            result += 1
print(result)
# x, y 관계에 유의
# 다음 세대는 이전 세대의 역순에 시계방향 회전 적용
        