p, m = map(int, input().split())
player, room = [], []

for _ in range(p):
    lv, nn = input().split()
    lv = int(lv)
    player.append([lv, nn])

for p in player:
    for rm in room:
        if rm[0][0]-10 <= p[0] <= rm[0][0]+10 and len(rm) < m:
            rm.append(p)
            break
    else:
        room.append([p])

for i in range(len(room)):
    if len(room[i]) == m:
        print('Started!')
    else:
        print('Waiting!')
    room[i].sort(key=lambda x: x[1])
    for j in room[i]:
        print(j[0], j[1])
