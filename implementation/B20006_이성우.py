n, m = map(int, input().split())
rooms = []

for _ in range(n):
    lvl, name = input().split()
    if len(rooms) == 0:
        rooms.append([[int(lvl), name]])
    else:
        for idx in range(len(rooms)):
            if rooms[idx][0][0] - 10 <= int(lvl) <= rooms[idx][0][0] + 10 and len(rooms[idx]) < m:
                rooms[idx].append([int(lvl), name])
                break
        else:
            rooms.append([[int(lvl), name]])

for idx in range(len(rooms)):
    if len(rooms[idx]) < m:
        print('Waiting!')
        tmp = sorted(rooms[idx], key = lambda x : x[1])
        for t in tmp:
            print(*t)
    else:
        print('Started!')
        tmp = sorted(rooms[idx], key = lambda x : x[1])
        for t in tmp:
            print(*t)
# print(rooms)