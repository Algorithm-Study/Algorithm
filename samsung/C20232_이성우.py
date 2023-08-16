import heapq

MAX_N = 2000

# 변수 선언
n, m, p = 0, 0, 0

# 각 토끼 id 기록
pid = [0] * (MAX_N + 1)

# 각 토끼 이동거리 기록
pw = [0] * (MAX_N + 1)

# 각 토끼 점프 횟수 기록
jump_cnt = [0] * (MAX_N + 1)

# 각 토끼 점수 기록
result = [0] * (MAX_N + 1)

# 각 토끼 현재 위치 기록
point = [(0, 0)] * (MAX_N + 1)

# 각 토끼 id를 인덱스 번호로 변환
id_to_idx = {}

# 각각의 경주에서 토끼가 달렸는지 여부 기록
is_runned = [0] * (MAX_N + 1)

# 하나를 제외한 모든 토끼의 점수를 더하는 쿼리를 편하게 하기 위해
# total_sum이라는 변수 추가
total_sum = 0


# rabbit 구조체.
class Rabbit:
    def __init__(self, x, y, j, pid):
        self.x = x
        self.y = y
        self.j = j
        self.pid = pid

    # 이동할 토끼를 결정하기 위한 정렬함수
    def __lt__(self, other):
        if self.j != other.j: 
            return self.j < other.j
        if self.x + self.y != other.x + other.y: 
            return self.x + self.y < other.x + other.y
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid


# 가장 긴 위치를 판단하기 위한 정렬함수
def compare(a, b):
    if a.x + a.y != b.x + b.y: 
        return a.x + a.y < b.x + b.y
    if a.x != b.x: 
        return a.x < b.x
    if a.y != b.y: 
        return a.y < b.y
    return a.pid < b.pid


# 경주 시작 준비 쿼리 처리
def init(inp):
    global n, m, p

    n, m, p, *rabbits = inp
    for i in range(1, p + 1):
        pid[i] = rabbits[i * 2 - 2]
        pw[i] = rabbits[i * 2 - 1]

        id_to_idx[pid[i]] = i
        point[i] = (1, 1)


# 위로 이동
def get_up_rabbit(cur_rabbit, dis):
    up_rabbit = cur_rabbit
    dis %= 2 * (n - 1)

    if dis >= up_rabbit.x - 1:
        dis -= (up_rabbit.x - 1)
        up_rabbit.x = 1
    else:
        up_rabbit.x -= dis
        dis = 0

    if dis >= n - up_rabbit.x:
        dis -= (n - up_rabbit.x)
        up_rabbit.x = n
    else:
        up_rabbit.x += dis
        dis = 0

    up_rabbit.x -= dis

    return up_rabbit


# 아래로 이동
def get_down_rabbit(cur_rabbit, dis):
    down_rabbit = cur_rabbit
    dis %= 2 * (n - 1)

    if dis >= n - down_rabbit.x:
        dis -= (n - down_rabbit.x)
        down_rabbit.x = n
    else:
        down_rabbit.x += dis
        dis = 0

    if dis >= down_rabbit.x - 1:
        dis -= (down_rabbit.x - 1)
        down_rabbit.x = 1
    else:
        down_rabbit.x -= dis
        dis = 0
    
    down_rabbit.x += dis

    return down_rabbit


# 왼쪽 이동
def get_left_rabbit(cur_rabbit, dis):
    left_rabbit = cur_rabbit
    dis %= 2 * (m - 1)

    if dis >= left_rabbit.y - 1:
        dis -= (left_rabbit.y - 1)
        left_rabbit.y = 1
    else:
        left_rabbit.y -= dis
        dis = 0

    if dis >= m - left_rabbit.y:
        dis -= (m - left_rabbit.y)
        left_rabbit.y = m
    else:
        left_rabbit.y += dis
        dis = 0

    left_rabbit.y -= dis

    return left_rabbit


# 오른쪽 이동
def get_right_rabbit(cur_rabbit, dis):
    right_rabbit = cur_rabbit
    dis %= 2 * (m - 1)

    if dis >= m - right_rabbit.y:
        dis -= (m - right_rabbit.y)
        right_rabbit.y = m
    else:
        right_rabbit.y += dis
        dis = 0

    if dis >= right_rabbit.y - 1:
        dis -= (right_rabbit.y - 1)
        right_rabbit.y = 1
    else:
        right_rabbit.y -= dis
        dis = 0
    
    right_rabbit.y += dis

    return right_rabbit


def copy_rabbit(rabbit):
    return Rabbit(rabbit.x, rabbit.y, rabbit.j, rabbit.pid)


# 경주 진행
def start_round(inp):
    global total_sum

    k, bonus = inp
    rabbit_pq = []

    for i in range(1, p + 1):
        is_runned[i] = False

    # 우선 p마리의 토끼들을 전부 우선순위 큐에 입력
    for i in range(1, p + 1):
        x, y = point[i]
        new_rabbit = Rabbit(x, y, jump_cnt[i], pid[i])
        heapq.heappush(rabbit_pq, new_rabbit)

    # 경주를 k회 진행합니다.
    for _ in range(k):
        # 우선순위가 가장 높은 토끼를 큐에서 추출
        cur_rabbit = heapq.heappop(rabbit_pq)
        
        # 해당 토끼를 상, 하, 좌, 우 4개의 방향으로 이동
        # 각각의 방향으로 이동시킨 후 최종 위치를 구하고
        # 가장 시작점으로부터 멀리 있는 위치를 탐색
        dis = pw[id_to_idx[cur_rabbit.pid]]
        nex_rabbit = copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0


        # 위로 이동
        up_rabbit = get_up_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지 갱신
        if compare(nex_rabbit, up_rabbit): 
            nex_rabbit = up_rabbit


        # 아래로 이동
        down_rabbit = get_down_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지 갱신
        if compare(nex_rabbit, down_rabbit): 
            nex_rabbit = down_rabbit


        # 왼쪽으로 이동
        left_rabbit = get_left_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지 갱신
        if compare(nex_rabbit, left_rabbit): 
            nex_rabbit = left_rabbit


        # 오른쪽으로 이동
        right_rabbit = get_right_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 갈 수 있다면 도착지 갱신
        if compare(nex_rabbit, right_rabbit): 
            nex_rabbit = right_rabbit

        # 토끼의 점프 횟수를 갱신해주고, 우선순위 큐에 푸시
        nex_rabbit.j += 1
        heapq.heappush(rabbit_pq, nex_rabbit)

        # 실제 point, jump_cnt 배열에도 값 갱신
        nex_idx = id_to_idx[nex_rabbit.pid]
        point[nex_idx] = (nex_rabbit.x, nex_rabbit.y)
        jump_cnt[nex_idx] += 1

        # 토끼가 달렸는지 여부 체크
        is_runned[nex_idx] = True

        # 토끼가 받는 점수는 (현재 뛴 토끼)만 (r + c)만큼 점수를 빼주고
        # 모든 토끼(total_sum)에게 (r + c)만큼 점수를 더함
        # 최종적으로 i번 토끼가 받는 점수는 result[i] + total_sum
        result[nex_idx] -= (nex_rabbit.x + nex_rabbit.y)
        total_sum += (nex_rabbit.x + nex_rabbit.y)

    # 보너스 점수를 받을 토끼 탐색
    # 이번 경주때 달린 토끼 중 가장 멀리있는 토끼 탐색
    bonus_rabbit = Rabbit(0, 0, 0, 0)
    while rabbit_pq:
        cur_rabbit = heapq.heappop(rabbit_pq)

        # 달리지 않은 토끼는 스킵
        if not is_runned[id_to_idx[cur_rabbit.pid]]: 
            continue

        if compare(bonus_rabbit, cur_rabbit):
            bonus_rabbit = cur_rabbit

    # 해당 토끼에게 bonus만큼 점수 추가
    result[id_to_idx[bonus_rabbit.pid]] += bonus


# 이동거리 변경
def power_up(inp):
    pid, t = inp
    idx = id_to_idx[pid]

    pw[idx] *= t


# 최고의 토끼 선정
def print_result():
    ans = 0
    for i in range(1, p + 1):
        ans = max(ans, result[i] + total_sum)

    print(ans)


q = int(input())
for _ in range(q):
    query, *inp = list(map(int, input().split()))

    # 경주 시작 준비 쿼리 처리
    if query == 100:
        init(inp)
    # 경주 진행
    if query == 200:
        start_round(inp)
    # 이동거리 변경
    if query == 300:
        power_up(inp)
    # 최고의 토끼 선정
    if query == 400:
        print_result()