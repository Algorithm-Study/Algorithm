from collections import deque
from collections import defaultdict

# 변수 초기화
s, p = map(int, input().split())
dna = list(input())
keys = ['A', 'C', 'G', 'T']
values = list(map(int, input().split()))
check = dict(zip(keys, values))
window = deque()
window_dict = defaultdict(int)
answer = 0

# deque 들어오고 나가는 문자열 확인해서 개수 확인
for idx, d in enumerate(dna):
    window.append(d)
    window_dict[d] += 1
    if len(window) >= p:
        for k in keys:
            # 조건에 부합하지 않으면 break
            if window_dict[k] < check[k]:
                break
        else:
            # 모두 부합하면 카운트
            answer += 1
        window_dict[window.popleft()] -= 1
print(answer)

# for문과 index 방법으로 deque없이도 더 빠르게 구현할 수 있다