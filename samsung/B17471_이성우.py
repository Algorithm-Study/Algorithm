from collections import deque
from itertools import combinations

# 변수 초기화
n = int(input())
people = [0] + list(map(int, input().split()))
arr = [[] for _ in range(n+1)]
answer = float('inf')
v = [_ for _ in range(1, n+1)]

# 그래프 생성
for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    arr[i].extend(tmp[1:])

# 그래프 탐색
def bfs(group):
    '''
    그룹의 모든 노드가 연결 됐는지 확인
    '''
    q = deque()
    q.append(group[0])
    visited = [False]*(n+1)
    visited[group[0]] = True
    
    while q:
        x = q.popleft()
        for nx in arr[x]:
            if nx in group and visited[nx] == False:
                q.append(nx)
                visited[nx] = True
    
    for g in group:
        if visited[g] == False:
            return False
    return True

for i in range(1, n//2+1):
    
    # 그룹 분할 및 최소값 탐색
    for group1 in combinations(v, i):
        group2 = [_ for _ in v if _ not in group1]
        
        if bfs(group1) and bfs(group2):
            p1 = sum(people[_] for _ in group1)
            p2 = sum(people[_] for _ in group2)
            
            answer = min(answer, abs(p1 - p2))

# 정답 출력
if answer == float('inf'):
    answer = -1
print(answer)