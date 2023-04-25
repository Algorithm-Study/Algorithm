from collections import deque

N, K = map(int, input().split())
data = list(input())
dqh, dqp = deque(), deque()
ans = 0
for idx, dt in enumerate(data):
    if dt == 'H':
        dqh.append(idx+K)
        while dqp:
            if dqp[0] >= idx:
                ans += 1
                dqh.pop()
                dqp.popleft()
                break
            else:
                dqp.popleft()
    else:
        dqp.append(idx+K)
        while dqh:
            if dqh[0] >= idx:
                ans += 1
                dqp.pop()
                dqh.popleft()
                break
            else:
                dqh.popleft()

print(ans)

# 문제 접근 방법
# # 햄버거와 사람의 덱을 만들어놓고 유효기간을 저장해놓기
# # 문자열을 읽으면서 덱과 비교