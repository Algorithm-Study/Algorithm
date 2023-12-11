import sys
input = sys.stdin.readline

# 초기값 설정
n = int(input().rstrip())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())
dp = [0]*(n+1)

for i in range(1, n+1):
    # 전날 하고 비교해서 큰 값
    dp[i] = max(dp[i], dp[i-1])
    end_day = i + t[i] - 1
    # 오늘 할 일이 기간 내에 끝나는지 확인
    if end_day <= n:
        # 끝나는 날의 이익을 어제의 이익에 오늘의 이익을 더한 값과 비교
        dp[end_day] = max(dp[end_day], dp[i-1] + p[i])
        
print(max(dp))