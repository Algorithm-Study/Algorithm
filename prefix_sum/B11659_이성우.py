import sys
# 이거 안하면 시간초과 뜸
input = sys.stdin.readline

total_num , problem_num = map(int, input().split())
problem_list = list(map(int,input().split()))
dp = [0]*(total_num+1)
for i in range(total_num):
    dp[i+1] += dp[i] + problem_list[i]

for j in range(problem_num):
    x, y = map(int, input().split())
    print(dp[y]-dp[x-1])


        