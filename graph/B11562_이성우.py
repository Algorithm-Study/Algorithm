import sys
input = sys.stdin.readline
INF = sys.maxsize

# 초기값 설정
n, m = map(int, input().split())
arr = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(1, n+1):
    arr[_][_] = 0

# 이동할 수 있으면 cost를 0으로 처리
# 없으면 1로 cost 표시
for _ in range(m):
    u, v, b = map(int, input().split())
    if b == 1:
        arr[u][v] = 0
        arr[v][u] = 0
    else:
        arr[u][v] = 0
        arr[v][u] = 1
        
# 플로이드 워셜로 최단 거리를 이동하는데 소요되는 cost 확인
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

# 정답 출력
for _ in range(int(input().rstrip())):
    s, e = map(int, input().split())
    print(arr[s][e])