from collections import deque
n, k = map(int, input().split())
endurance = list(map(int, input().split()))
rails = [0] * (2*n)
zero  = endurance.count(0)
stage = 1
queue = deque()
while zero < k:
    # 레일 회전
    endurance = [endurance[-1]] + endurance[:-1]
    rails = [rails[-1]] + rails[:-1]
    new_queue = []
    if rails[n-1] != 0:
        rails[n-1] = 0
    # 이동 가능 여부 체크
    while queue:
        idx = queue.popleft()
        if idx+ 1 != 2*n:
            idx += 1
        else:
            idx = 0
        # 회전으로 빈 레일 제거
        if rails[idx] == 0:
            continue
        if idx != 2*n-1:
            next = idx + 1
        else:
            next = 0
        if rails[next] == 0 and endurance[next] > 0:
            rails[idx] = 0
            endurance[next] -= 1
            if next != n-1:
                new_queue.append(next)
                rails[next] = 1
        else:
            new_queue.append(idx)
    queue = deque(new_queue)
    # 새로운 로봇 넣는지 여부 확인
    if rails[0] == 0 and endurance[0] > 0:
        rails[0] = 1
        endurance[0] -= 1
        queue.append(0)
    zero = endurance.count(0)
    stage += 1
print(stage - 1)

# 내구도의 감소는 로봇의 이동(도착 레일 위치), 새로운 로봇 투입의 경우에만 이루어짐