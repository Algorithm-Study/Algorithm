import sys
input = sys.stdin.readline

# 초기값 설정
n = int(input())
m = int(input())

# 플로이드 워셜과 직전 경로를 담는 배열 생성
dp = [[float('inf')]*(n+1) for _ in range(n+1)]
path = [[-1]*(n+1) for _ in range(n+1)]

# 조건 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)
    path[a][b] = a

# 플로이드 워셜 실행과 직전 경로 체크
for k in range(1, n+1):
    dp[k][k] = 0
    path[k][k] = -1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                path[i][j] = path[k][j]

# 전체 관계 프린트                
for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == float('inf'):
            print(0, end=' ')
        else:
            print(dp[i][j], end=' ')
    print()

# 경로 역추적 후 프린트
for i in range(1, n+1):
    for j in range(1, n+1):
        if path[i][j] == -1:
            print(0)
            continue
        v = j
        answer = []
        while True:
            if v == i:
                break
            answer.append(v)
            v = path[i][v]
        print(len(answer)+1, i, *answer[::-1])