p, m = map(int, input().split())
rooms = [[]]
for i in range(p):
    level, nickname = input().split()
    level = int(level)
    if i == 0:
        rooms[0].append([level, nickname])
        continue
    for j in range(len(rooms)):
        if len(rooms[j]) == m:
            continue
        if rooms[j][0][0] - 10 <= level <=  rooms[j][0][0] + 10:
            rooms[j].append([level,nickname])
            break
    else:
        rooms.append([[level, nickname]])

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    # 사전 순으로 출력이므로 정렬
    room.sort(key = lambda x: x[1])
    for r in room:
        print(r[0], r[1])

# rooms 구조 -> [[[레벨, 아이디], [레벨, 아이디], [레벨, 아이디]],[[레벨, 아이디], [레벨, 아이디]], ...]
# 정원이 여유가 있고 레벨차가 10이내인 경우 방에 추가
# 모든 사람들의 입장이 끝난 다음 정원 여부에 따라서 Started! Waiting! 각 출력 후 방에 있는 사람 닉네임 순으로 정렬 후 출력