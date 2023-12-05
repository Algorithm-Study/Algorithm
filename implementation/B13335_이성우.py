from collections import deque
# 초기값 설정
n, w, l = map(int, input().split())
arr = deque(map(int, input().split()))
dq = deque([0]*w)
sum_ = 0
answer = 0

# 트럭이 존재할 때
while arr:
    num = arr.popleft()
    sum_ -= dq.popleft()
    # 다리 위의 무게가 초과되면 트럭 안올라감
    if sum_ + num > l:
        dq.append(0)
        arr.appendleft(num)
    # 올라갈 수 있으면 올라감
    else:
        dq.append(num)
        sum_ += num
    answer += 1
    
print(answer+len(dq))