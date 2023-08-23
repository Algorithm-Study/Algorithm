import copy
ways = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
fish = {}
field = [[] for _ in range(4)]
#입력 받기
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0,8,2):
        fish[info[j]] = info[j+1] - 1
        field[i].append(info[j])
max_eat = 0
# 필드 내 해당 물고기 존재하는지 여부
def is_exist(seq, field) -> list:
    for i in range(4):
        for j in range(4):
            if field[i][j] == seq:
                return [i,j]
    return [-1,-1]
    
def turn(shark_x,shark_y, current, field, fish):
    global max_eat
    current += field[shark_x][shark_y]
    shark_dir = fish[field[shark_x][shark_y]]
    field[shark_x][shark_y] = 0
    max_eat = max(max_eat, current)
    for seq in range(1,17):
        x,y = is_exist(seq, [x[:] for x in field])
        # 먹혀서 없는 경우
        if [x,y] == [-1,-1]:
            continue
        dir = fish[seq]
        # 믈고기 이동
        for i in range(8):
            ndir = (dir + i)%8
            nx = x+ ways[ndir][0]
            ny = y+ ways[ndir][1]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue
            if nx == shark_x and ny == shark_y:
                continue
            fish[seq] = ndir
            field[nx][ny], field[x][y] = field[x][y], field[nx][ny]
            break
    #상어 이동
    for i in range(1,4):
        nshark_x = shark_x + ways[shark_dir][0]*i
        nshark_y = shark_y + ways[shark_dir][1]*i
        if nshark_x < 0 or nshark_x >= 4 or nshark_y < 0 or nshark_y >= 4 or field[nshark_x][nshark_y] == 0:
            continue
        turn(nshark_x, nshark_y, current, [x[:] for x in field], copy.deepcopy(fish))
        
turn(0,0,0,field,fish)
print(max_eat)

# 재귀 함수 과정에서 값이 변하지 않도록 설정하기