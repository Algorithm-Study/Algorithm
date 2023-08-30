dx = [0,0,-1,1]
dy = [1,-1,0,0]
convert = {0:1,1:0,2:3,3:2}
n, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
record = [[[] for _ in range(n)] for _ in range(n)]
pieces = []
for i in range(1,K+1):
    x, y, way = list(map(int, input().split()))
    pieces.append([x-1,y-1, way-1])
    record[x-1][y-1].append(i)
turns = 0
max_height = 1
while turns < 1000:
    # 종료 조건을 달성한 경우
    if max_height >= 4:
        break
    # 순차적으로 이동 진행
    for idx, piece in enumerate(pieces):
        x,y,way = piece
        # 몇번째 인지 알아야 함
        pos = record[x][y].index(idx+1)
        nx = x + dx[way]
        ny = y + dy[way]
        # 범위를 벗어난 경우
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            way = convert[way]
            pieces[idx][2] = way
            nx = x + dx[way]
            ny = y + dy[way]
            # 반대편 이동이 가능한 경우(파란 블록만 아니면 됨)
            if field[nx][ny] == 0:
                for p in record[x][y][pos:]:
                    pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:]
                record[x][y] = record[x][y][:pos]
            elif field[nx][ny] == 1:
                for p in record[x][y][pos:]:
                    pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:][::-1]
                record[x][y] = record[x][y][:pos]
        # 파란 블록인 경우
        elif field[nx][ny] == 2:
            way = convert[way]
            pieces[idx][2] = way
            nx = x + dx[way]
            ny = y + dy[way]
            # 반대편 이동이 가능한 경우(파란 블록이랑 외곽만 아니면 됨)
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            elif field[nx][ny] == 0:
                for p in record[x][y][pos:]:
                    pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:]
                record[x][y] = record[x][y][:pos]
            elif field[nx][ny] == 1:
                for p in record[x][y][pos:]:
                    pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:][::-1]
                record[x][y] = record[x][y][:pos]
        # 빨간 블록인 경우
        elif field[nx][ny] == 1:
            for p in record[x][y][pos:]:
                pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:][::-1]
                record[x][y] = record[x][y][:pos]
        # 일반 블록인 경우
        else:
            for p in record[x][y][pos:]:
                pieces[p-1] = [nx,ny, pieces[p-1][2]]
                record[nx][ny] = record[nx][ny] + record[x][y][pos:]
                record[x][y] = record[x][y][:pos]
        max_height = max(max_height, len(record[nx][ny]))
    turns += 1
if turns < 1000:
    print(turns)
else:
    print(-1)