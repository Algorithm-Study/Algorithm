m, t = map(int, input().split())
tmp_loc = list(map(int, input().split()))
pac_loc = (tmp_loc[0] - 1, tmp_loc[1] - 1)
monster_board = [[[] for _ in range(4)] for _ in range(4)]
for _ in range(m):
    tmp = list(map(int, input().split()))
    # 몬스터 보드에 표기한다. 해당 위치에는 몬스터가 다음에 갈 방향만을 표기한다.
    monster_board[tmp[0] - 1][tmp[1] - 1].append(tmp[2] - 1)

directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

# 몬스터 입장에서 장애물에 해당하는 팩맨과 시체의 위치를 나타내는 보드를 생성
# 팩맨 -> 4, 시체 -> 3 (2턴 이후 소멸을 구현)
pac_board = [[0] * 4 for _ in range(4)]
pac_board[pac_loc[0]][pac_loc[1]] = 1

dead_board = [[0] * 4 for _ in range(4)]
rounds = 0
while rounds < t:

    # 몬스터 복제 시도
    # 현 몬스터의 위치와 정보를 그대로 담아둔다.
    egg_board = [[[] for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            egg_board[r][c] = monster_board[r][c]

    # 몬스터 위치는 초기화 해도 됨. 이동을 구현하기 위해 알이 된 보드를 활용.
    monster_board = [[[] for _ in range(4)] for _ in range(4)]

    # 몬스터의 이동
    # 몬스터 보드를 전체를 돌면서
    for r in range(4):
        for c in range(4):
            # 몬스터가 존재한다면
            if egg_board[r][c]:
                # 하나를 빼온다.
                for now_dir in egg_board[r][c]:
                    # 8방향을 도는데
                    isMoved = False
                    for dir_idx in range(8):
                        next_dir = (now_dir + dir_idx) % 8
                        nr = r + directions[next_dir][0]
                        nc = c + directions[next_dir][1]
                        if 0 <= nr < 4 and 0 <= nc < 4:
                            # 팩맨이 없고 사체도 없는가?
                            if pac_board[nr][nc] == 0 and dead_board[nr][nc] == 0:
                                # 가려던 곳으로 바뀐 방향을 넣어준다.
                                monster_board[nr][nc].append(next_dir)
                                isMoved = True
                                break
                    # 만약 움직임이 없었다면
                    if not isMoved:
                        # 그 자리에 다시 둔다
                        monster_board[r][c].append(now_dir)
    # 팩맨의 이동. 상-좌-하-우의 우선순위에 유의하고
    # 이동시에만 먹으며 이동 간 가장 많은 몬스터를 먹어야 하므로
    # 스택 구현. 최초는 현재 팩맨의 위치와 4방향을 순서에 따라 넣어줌.
    pac_directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # (r, c, 먹은 수, 지나간 경로)
    best_move = (0, 0, -1, [])
    pac_r, pac_c = pac_loc
    move_stack = []
    for idx in range(4):
        move_stack.append(pac_directions[idx])
        for idx in range(4):
            move_stack.append(pac_directions[idx])
            for idx in range(4):
                move_stack.append(pac_directions[idx])
                pac_r, pac_c = pac_loc
                # 3턴 간의 움직임이 정해지면 이대로 움직여본다.
                steps = 0
                eat = 0
                way = []
                while 1:
                    if steps == 3:
                        # 만약 제일 잘 먹은거라면
                        if best_move[2] < eat:
                            # best 갱신
                            best_move = (pac_r, pac_c, eat, move_stack[:])
                        break
                    pac_r += move_stack[steps][0]
                    pac_c += move_stack[steps][1]
                    # 범위를 넘어가지 않으면
                    if 0 <= pac_r < 4 and 0 <= pac_c < 4:
                        steps += 1
                        # 그 때까지 먹은 수를 기록하고 다음 스텝으로 넘긴다.
                        # 단, 이미 갔다 왔어서 먹은거라면 안됨.
                        if (pac_r, pac_c) not in way:
                            eat += len(monster_board[pac_r][pac_c])
                        way.append((pac_r, pac_c))
                    else:
                        # 범위를 나간다면 유효하지 않는 경로임.
                        break
                move_stack.pop()
            move_stack.pop()
        move_stack.pop()
    # 베스트 이동을 토대로 몬스터 시체를 남긴다
    # 저장한 경로를 바탕으로 시체를 남기고 팩맨의 위치를 갱신한다.
    pac_r, pac_c = pac_loc
    pac_board[pac_r][pac_c] = 0
    for way in best_move[3]:
        pac_r += way[0]
        pac_c += way[1]
        # 몬스터가 존재한다면
        if monster_board[pac_r][pac_c]:
            # 칸 째로 날려버리자
            monster_board[pac_r][pac_c] = []
            # 시체를 남긴다
            dead_board[pac_r][pac_c] = 3
    # 팩맨 위치 재설정
    pac_loc = (best_move[0], best_move[1])
    pac_board[best_move[0]][best_move[1]] = 1
    # 몬스터 알의 부화
    # 알 리스트를 돌면서 몬스터로 편입
    for r in range(4):
        for c in range(4):
            # 알이 존재한다면
            if egg_board[r][c]:
                monster_board[r][c].extend(egg_board[r][c])
    # 시체 소멸 구현
    for r in range(4):
        for c in range(4):
            if 0 < dead_board[r][c]:
                dead_board[r][c] -= 1
    rounds += 1
# 정답은 몬스터 마리수
answer = 0
for r in range(4):
    for c in range(4):
        answer += len(monster_board[r][c])

print(answer)
# 시체가 3턴 유지되어야 한다는 점에 주의할 것!