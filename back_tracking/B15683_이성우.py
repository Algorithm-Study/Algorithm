from copy import deepcopy

def count_blind_spot(office, cctv, idx, count):
    global min_blind_spot
    if idx == len(cctv):
        # 모든 CCTV의 방향을 조합한 경우
        min_blind_spot = min(min_blind_spot, count)
        return
    x, y, kind = cctv[idx]
    for directions in cctv_directions[kind]:
        watched_office = deepcopy(office)  # 사무실 상태 복사
        # 현재 CCTV의 종류에 해당하는 모든 방향 조합에 대해 감시 영역 표시
        watch(watched_office, x, y, directions)
        count_blind_spot(watched_office, cctv, idx + 1, count_blind(watched_office))
            
def watch(office, x, y, directions):
    for direction in directions:
        nx, ny = x, y
        while True:
            nx += dx[direction]
            ny += dy[direction]
            if 0 <= nx < N and 0 <= ny < M:
                if office[nx][ny] == 6:  # 벽을 만나면 종료
                    break
                if office[nx][ny] == 0:  # CCTV의 영향이 아닌 빈 칸이면 감시 영역으로 표시
                    office[nx][ny] = -1
            else:
                break
                
def count_blind(office):
    count = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                count += 1
    return count

# 입력 받기
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# CCTV 정보 저장
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j, office[i][j]))

# CCTV의 방향 조합
cctv_directions = [
    [],  # 0번 CCTV (사용하지 않음)
    [[0], [1], [2], [3]],  # 1번 CCTV (한 방향)
    [[0, 2], [1, 3]],  # 2번 CCTV (두 방향)
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3번 CCTV (직각 방향)
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],  # 4번 CCTV (세 방향)
    [[0, 1, 2, 3]]  # 5번 CCTV (네 방향)
]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

min_blind_spot = float('inf')

# CCTV의 방향 조합하여 사각 지대의 최소 크기 구하기
count_blind_spot(office, cctv, 0, count_blind(office))

print(min_blind_spot)
