from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

# 변수 초기화
n, q = map(int, input().split())
arr = [[] for _ in range(n+1)]

# 입력 동영상 유사도 설정
for _ in range(n-1):
    a, b, u = map(int, input().split())
    arr[a].append((b, u))
    arr[b].append((a, u))

# 그래프 탐색
for _ in range(q):
    k, v = map(int, input().split())
    visited = [False]*(n+1)
    visited[v] = True
    answer = 0
    q = deque()
    q.append((v, INF))
    
    # 그래프를 탐색하면서 유사도 갱신
    while q:
        v, u = q.popleft()
        for nv, nu in arr[v]:
            nu = min(u, nu)
            
            # 갱신된 유사도가 k보다 크면 정답 체크 후 계속 탐색
            if nu >= k and not visited[nv]:
                answer += 1
                q.append((nv, nu))
                visited[nv] = True
    print(answer)