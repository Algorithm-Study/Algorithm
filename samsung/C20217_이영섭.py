from itertools import product
from copy import deepcopy

direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def copy_monster_try():
    # 몬스터 복제 시도
    # # 알을 복제한다. 복제 됐을 때의 방향을 가진다.
    for cx, cy, cd in monster:
        egg.append((cx, cy, cd))


def move_monster():
    # 몬스터 이동
    # # 움직이려는 칸에 몬스터 시체가 있거나, 팩맨이 있거나, 격자를 벗어나면 반시계 방향으로 45도 회전하다가
    # # 가능하면 자신의 방향으로 한 칸 이동
    global monster
    for idx, [cx, cy, cd] in enumerate(monster):
        nd = cd
        for i in range(8):
            nx, ny = cx + direction[nd][0], cy + direction[nd][1]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or (nx == px and ny == py) or corpse[(nx, ny)] > 0:
                nd = (nd + 1) % 8
                continue
            else:
                monster[idx] = [nx, ny, nd]
                monster_dict[(cx, cy, cd)] -= 1
                monster_dict[(nx, ny, nd)] += 1
                break


def move_packman():
    # 팩맨 이동
    # # 이동 과정에서 격자를 벗어나지 않는 경우만 고려
    # # 상(-1, 0) - 좌(0, -1) - 하(1, 0) - 우(0, 1)
    # # 3칸 이동하면서 만난 몬스터만 먹고 시체를 남긴다.
    global px, py, monster
    news = [0, 2, 4, 6]
    bf = list(product(news, repeat=3))
    cx, cy, mx, my, max_val = px, py, px, py, -1
    route = []

    # 경로 찾기
    for case in bf:
        new_monster_dict = deepcopy(monster_dict)
        nx, ny, cnt = cx, cy, 0
        for i in case:
            nx, ny = nx + direction[i][0], ny + direction[i][1]
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                break
            for nx, ny, d in [(nx, ny, d) for d in range(8)]:
                if new_monster_dict[(nx, ny, d)] > 0:
                    cnt += new_monster_dict[(nx, ny, d)]
                    new_monster_dict[(nx, ny, d)] = 0
        else:
            if cnt > max_val:
                mx, my = nx, ny
                max_val = cnt
                route = case

    # 경로 이동
    new_monster, out_monster = [], []
    nx, ny = cx, cy
    for i in route:
        nx, ny = nx + direction[i][0], ny + direction[i][1]
        for nx, ny, d in [(nx, ny, d) for d in range(8)]:
            if monster_dict[(nx, ny, d)] > 0:
                out_monster.append([nx, ny, d])
                monster_dict[(nx, ny, d)] = 0
                corpse[(nx, ny)] = 3
    new_monster = [item for item in monster if item not in out_monster]
    monster = new_monster[:]
    px, py = mx, my


def remove_corpse():
    # 몬스터 시체 소멸
    # # 시체는 2턴동안 유지된다.
    for i in range(4):
        for j in range(4):
            if corpse[(i, j)] > 0:
                corpse[(i, j)] -= 1


def copy_monster_complete():
    # 몬스터 복제 완성
    # # 알이었던 몬스터가 부화한다.
    global egg
    for cx, cy, cd in egg:
        monster.append([cx, cy, cd])
        monster_dict[(cx, cy, cd)] += 1
    egg = []


m, t = map(int, input().split())
px, py = map(int, input().split())
px, py = px - 1, py - 1
monster, egg = [], []
monster_dict = {(i, j, d): 0 for i in range(4) for j in range(4) for d in range(8)}
corpse = {(i, j): 0 for i in range(4) for j in range(4)}

for _ in range(m):
    r, c, d = map(int, input().split())
    monster.append([r - 1, c - 1, d - 1])
    monster_dict[(r - 1, c - 1, d - 1)] += 1

for _ in range(t):
    copy_monster_try()
    move_monster()
    move_packman()
    remove_corpse()
    copy_monster_complete()

print(len(monster))
