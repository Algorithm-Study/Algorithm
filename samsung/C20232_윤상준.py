import sys
input = sys.stdin.readline
ways = [(-1,0),(0,-1),(1,0),(0,1)]
Q = int(input())
commands = list(map(int, input().split()))
n, m, p = commands[1],commands[2], commands[3]
rabbit = {}
rabbit_score = {}
for i in range(0,len(commands[4:]),2):
    # pid, distance, x, y, count
    rabbit[commands[4+i]] = [commands[4+i],commands[5+i], 0,0, 0]
    rabbit_score[commands[4+i]] = 0
queries = []
for _ in range(Q-1):
    queries.append(list(map(int, input().split())))
for commands in queries:
    if commands[0] == 400:
        break
    if commands[0] == 200:
        for r in rabbit:
            rabbit[r][4] = 0
        for _ in range(commands[1]):
            #print(rabbit_score)
            rabbit = dict(sorted(rabbit.items(), key= lambda x: (x[1][4], x[1][2]+ x[1][3], x[1][2], x[1][3], x[0])))
            rabbit[list(rabbit.keys())[0]][4] += 1
            x, y= rabbit[list(rabbit.keys())[0]][2], rabbit[list(rabbit.keys())[0]][3]
            choices = []
            #print(f'START {x} {y}')
            for i in range(4):
                dx = (x+ rabbit[list(rabbit.keys())[0]][1] * ways[i][0])%(2*(n-1))
                dy = (y+ rabbit[list(rabbit.keys())[0]][1] * ways[i][1])%(2*(m-1))
                if 0<= dx < n and 0 <=  dy < m:
                    choices.append((dx+dy, dx,dy))
                # 위로 이동인 경우
                elif i == 0:
                    dx = n - dx %(n-1) - 1
                    choices.append((dx+dy, dx, dy))
                # 좌로 이동한 경우
                elif i == 1:
                    dy = m - dy %(m-1) - 1
                    choices.append((dx+dy, dx, dy))
                # 우로 이동한 경우
                elif i == 2:
                    dx = n - (dx - (n-1-x)) - 1
                    choices.append((dx+dy, dx, dy))
                # 아래로 이동한 경우
                else:
                    dy = m - (dy - (m-1 -y)) - 1
                    choices.append((dx+dy, dx, dy))
            #print(choices)
            #print('='*20)
            choices.sort(key = lambda x: (-x[0], -x[1], -x[2]))
            rabbit[list(rabbit.keys())[0]][2], rabbit[list(rabbit.keys())[0]][3] = choices[0][1], choices[0][2]
            for r in rabbit_score:
                if r != rabbit[list(rabbit.keys())[0]][0]:
                    rabbit_score[r] += choices[0][0] + 2
        rabbit = dict(sorted(rabbit.items(), key= lambda x: (-(x[1][2]+ x[1][3] ), -x[1][2], -x[1][3], -x[0])))
        for r in rabbit:
            if rabbit[r][4] != 0:
                rabbit_score[r] += commands[2]
                break

    elif commands[0] == 300:
        rabbit[commands[1]][1] = rabbit[commands[1]][1] * commands[2]

rabbit_score = dict(sorted(rabbit_score.items(), key= lambda x: -x[1]))
print(rabbit_score[list(rabbit_score.keys())[0]])

###################################### 빠른 코드 ######################################
import sys
input = sys.stdin.readline

def jump(location, speed, boundary):
    return boundary - abs(boundary - (location + speed) % (boundary * 2))

def left_jump(row, col, speed):
    col = jump(col_boundary * 2 - col, speed, col_boundary)
    return row, col

def right_jump(row, col, speed):
    col = jump(col, speed, col_boundary)
    return row, col

def up_jump(row, col, speed):
    row = jump(row_boundary * 2 - row, speed, row_boundary)
    return row, col

def down_jump(row, col, speed):
    row = jump(row, speed, row_boundary)
    return row, col

def contest(params):
    global bit
    K, S = map(int, params)

    # 뛰지 않은 모든 토끼에게 점수 부여 -> 뛴 토끼에게 - 점수를 부여하고, 마지막에 모두에게 누적 점수 부여
    accum_score = 0

    # 승자는 이번 라운드에 뛴 적 있는 토끼 중에서만 고른다 -> 뛴 토끼 set으로 관리
    jumped_rabbit = set()

    for _ in range(K):

        # 비었다 -> 모든 토끼가 한번씩 뛰었다 -> 다른 큐로 넘겨줄 차례
        if not queues[bit]:
            bit ^= 1
            queues[bit].sort(key = rabbit_comparator, reverse= True)
        
        rabbit_id = queues[bit].pop()
        row, col, speed = row_dict[rabbit_id], col_dict[rabbit_id], speed_dict[rabbit_id]
        # left_jump, right_jump 등을 통해 나온 좌표를 가지고 jump_comparator로 비교해 최대 점수를 가지는 좌표 도출
        nrow, ncol = max([do_jump(row, col, speed) for do_jump in jump_directions], key = jump_comparator)

        # 좌표 업데이트
        row_dict[rabbit_id] = nrow
        col_dict[rabbit_id] = ncol

        # 점수 업데이트 (+2 는 행렬 번호가 0이 아닌 1부터 시작하기 때문)
        accum_score += nrow + ncol + 2
        score_dict[rabbit_id] -= nrow + ncol + 2

        # 큐에 추가
        queues[bit^1].append(rabbit_id)

        jumped_rabbit.add(rabbit_id)

    for rabbit_id in score_dict.keys():
        score_dict[rabbit_id] += accum_score
    
    winner = max(jumped_rabbit, key = rabbit_comparator)

    score_dict[winner] += S

def accelerate(params):
    rabbit_id, number = map(int, params)
    speed_dict[rabbit_id] *= int(number)

Q = int(input().strip())
_, N, M, P, *rabbits = input().split()
col_boundary = int(M) - 1
row_boundary = int(N) - 1
row_dict = dict()
col_dict = dict()
speed_dict = dict()
score_dict = dict()
rabbit_comparator = lambda x: (row_dict[x] + col_dict[x], row_dict[x], col_dict[x], x)

# 큐 = [[짝수번 뛴 애들], [홀수번 뛴 애들]]
queues = [[], []]
# 모든 토끼가 다 뛰면 비트를 바꿔줌 -> queues[bit] 이 비면 bit ^ 1 하면 됨.
bit = 0

for index in range(0, len(rabbits), 2):
    rabbit_id, speed = map(int, rabbits[index:index+2])
    row_dict[rabbit_id] = col_dict[rabbit_id] = 0
    speed_dict[rabbit_id] = speed
    score_dict[rabbit_id] = 0
    queues[0].append(rabbit_id)

queues[0].sort(key = rabbit_comparator, reverse = True)

jump_directions = (left_jump, right_jump, up_jump, down_jump)
jump_comparator = lambda x: (x[0] + x[1], x[0], x[1]) # 행+열 번호, 행 번호, 열 번호 순서

query_dict = {
    "200": contest,
    "300": accelerate
}

for _ in range(Q-2):
    query, *params = input().split()
    query_dict[query](params)

print(max(score_dict.values()))