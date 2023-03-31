from collections import deque

# 맵 생성
N = int(input())
maps = [[0 for _ in range(N)] for _ in range(N)]
# print(maps)

# 사과 추가
apple_num = int(input())
for _ in range(apple_num):
    apple_row, apple_col = map(int,input().split())
    maps[apple_row-1][apple_col-1] = 'a'
# print(maps)

# moves 배열 생성
move_num = int(input())
moves = deque()
for _ in range(move_num):
    sec, direction = input().split()
    moves.append([int(sec), direction])
# print(moves)

# 초기 설정
maps[0][0] = 'b'
x, y = 0, 0
bam = deque()
bam.append([0,0])
second = 0

# 방향 조건 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
i = 0

# print('_'*N*2)
while True:
    
    # 디버깅
    # print(str(second)+'초')
    # for _ in maps:
    #     print(*_)    
    # print('_'*N*2)

    # 보고 있는 방향으로 맵 탐색
    second += 1
    nx = x + dx[i%4]
    ny = y + dy[i%4]
    # 이동이 가능하면
    if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] != 'b':
        
        # 사과가 있다면 사과를 먹고 성장
        if maps[nx][ny] == 'a':
            maps[nx][ny] = 'b'
            bam.append([nx, ny])
            
        # 사과가 없다면 몸통도 이동
        else:
            maps[nx][ny] = 'b'
            bam.append([nx, ny])
            ox, oy = bam.popleft()
            maps[ox][oy] = 0
            
        # 현재 위치 재설정
        x, y = nx, ny
        
    # 못 움직이면 종료
    else:
        break
    
    # 움직이고 조건 시간이 되면 방향 전환
    if moves and second == moves[0][0]:
        if moves[0][1] == 'D':
            i += 1
        else:
            i -= 1
        moves.popleft()

print(second)

# 1행1열부터 시작인데 0행0열부터 시작인 줄 알고
# 초기 변수를 잘못 생성해서 헤맸음