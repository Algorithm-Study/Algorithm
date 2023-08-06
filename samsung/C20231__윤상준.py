from collections import deque
n,m,k = map(int, input().split())
cannons = [list(map(int, input().split())) for _ in range(n)]   # 각 포납 공격력
attacks = [[0]*m for _ in range(n)]  # 각 포탑 공격 이력
laser = [(0, 1),(1, 0),(0, -1),(-1, 0)] # 공격 방향 우선 순위 우->하->좌->상
explode = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
for i in range(1, k+1):
    attack_list = []
    for x in range(n):
        for y in range(m):
            # 공격이 가능한 포탑인 경우
            if cannons[x][y] != 0:
                attack_list.append((cannons[x][y], attacks[x][y], x+y, y))
    # 종료조건 : 남은 포탑이 1이하인 경우
    if len(attack_list) <= 1:
        break
    # 공격자 선택하기
    attack_list.sort(key = lambda x: (x[0], -x[1], -x[2], -x[3]))
    attacker = (attack_list[0][2] - attack_list[0][3], attack_list[0][3])
    cannons[attacker[0]][attacker[1]] += n+m    # 공격력 갱신
    attacks[attacker[0]][attacker[1]] = i    # 공격 이력 갱신
    # 공격 당하는 자 선택하기
    attacked_list = sorted(attack_list[1:], key = lambda x: (-x[0], x[1], x[2], x[3]))
    attacked = (attacked_list[0][2] - attacked_list[0][3], attacked_list[0][3])
    #레이저 공격 확인
    queue = deque()
    queue.append([attacker[0], attacker[1], []])
    visited = [[0]*m for _ in range(n)]
    visited[attacker[0]][attacker[1]] = 1
    moves, flag = [], 0
    # 레이저 경로 계산
    while queue:
        x, y, record = queue.popleft()
        for k in range(4):
            # 범위 밖인 경우 수정
            nx = (x + laser[k][0]) % n
            ny = (y + laser[k][1]) % m
            if cannons[nx][ny] == 0 or visited[nx][ny] == 1:
                continue
            # 공격 대상에 도착한 경우
            if (nx, ny) == attacked:
                moves = record + [(nx, ny)]
                flag = 1
                break
            queue.append([nx, ny, record + [(nx, ny)]])
            visited[nx][ny] = 1
        if flag:
            break
    # 레이저 공격(가능한 경우)
    if moves:
        for x, y in moves[:-1]:
            cannons[x][y] = max(0,cannons[x][y] - cannons[attacker[0]][attacker[1]]//2)
        cannons[moves[-1][0]][moves[-1][1]] = max(0, cannons[moves[-1][0]][moves[-1][1]] - cannons[attacker[0]][attacker[1]])
    # 포탄 공격
    else:
        x, y = attacked
        moves.append((x,y))
        cannons[x][y] = max(0,cannons[x][y] - cannons[attacker[0]][attacker[1]])
        for k in range(8):
            # 범위 밖인 경우 수정
            nx = (x + explode[k][0]) % n
            ny = (y + explode[k][1]) % m
            moves.append((nx,ny))
            # 공격자는 공격 여파로부터 무효이므로 예외 처리
            if (nx, ny) != attacker:
                cannons[nx][ny] = max(0,cannons[nx][ny] - cannons[attacker[0]][attacker[1]]//2)
    # 포탑 정비
    for x in range(n):
        for y in range(m):
            # 공격한 포탑이나 공격당한 or 파괴된 포합이 아닌 경우
            if (x,y) in moves or (x, y) == attacker or cannons[x][y] == 0:
                continue
            cannons[x][y] += 1
# 가장 강한 캐논 출력
print(max([max(x) for x in cannons]))
