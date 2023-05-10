import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
m = int(input())
dp = [[0 if x != y else 1 for x in range(n)] for y in range(n)]
for i in range(n):
    for j in range(n-i):
        start, end = j, j+i
        if start == end:
            continue
        if sequence[start] == sequence[end]:
            if start+1 == end or dp[start+1][end-1] == 1:
                dp[start][end] = 1
            
for _ in range(m):
    start, end = map(int, input().split())
    print(dp[start-1][end-1])

# 팰린드롬의 규칙을 활용하여 양쪽을 제거한 형태가 팰린드롬인지 체크
# 길이가 1,2인 경우에 대한 처리를 진행하면 문제해결 가능