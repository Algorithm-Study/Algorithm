ways = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())
field = [[[] for _ in range(N)] for _ in range(N)]
fires = []
# 파이어볼 입력 받기
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fires.append((r-1, c-1,m,s,d))
# K번 이동하기
for _ in range(K):
    # 불 이동
    while fires:
        r, c, m, s, d = fires.pop()
        r = (r + s * ways[d][0]) % N
        c = (c + s * ways[d][1]) % N
        field[r][c].append((m, s, d))
    # 각 위치별 불의 갯수 확인
    for i in range(N):
        for j in range(N):
            num = len(field[i][j])
            if num >= 2:
                total_mass, total_speed, odd, even = 0, 0, 0, 0
                while field[i][j]:
                    m, s, d = field[i][j].pop()
                    total_mass += m
                    total_speed += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                # 분할 적용
                if even == num or odd == num:
                    queue = [0, 2, 4, 6]
                else:
                    queue = [1, 3, 5, 7]
                average_mass, average_speed = total_mass//5, total_speed//num
                if average_mass:
                    for k in range(4):
                        fires.append((i, j, average_mass, average_speed, queue[k]))
            elif num == 1:
                m, s, d = field[i][j].pop()
                fires.append((i, j, m, s, d))
total = sum([x[2] for x in fires])
print(total)

# 제시된 조건에 맞게 파이어볼을 분할하면 되는 문제