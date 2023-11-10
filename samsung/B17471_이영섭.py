from itertools import combinations
from collections import deque, defaultdict


def bfs(case):
    st = case[0]
    dq = deque()
    dq.append(st)
    visit = set([st])
    b_sum = 0

    while dq:
        cx = dq.popleft()
        b_sum += people[cx]
        for nx in people_dict[cx]:
            if nx not in visit and nx in case:
                dq.append(nx)
                visit.add(nx)
    return b_sum, len(visit)


n = int(input())
people = list(map(int, input().split()))
people_dict = defaultdict(list)
ans = float('inf')

for i in range(n):
    ip = list(map(int, input().split()))
    for idx in range(1, ip[0]+1):
        people_dict[i].append(ip[idx] - 1)

for i in range(1, n//2 + 1):
    bf = list(combinations(range(n), i))
    for case in bf:
        sum1, val1 = bfs(case)
        sum2, val2 = bfs([i for i in range(n) if i not in case])
        if val1 + val2 == n:
            ans = min(ans, abs(sum1 - sum2))

if ans != float('inf'):
    print(ans)
else:
    print(-1)
