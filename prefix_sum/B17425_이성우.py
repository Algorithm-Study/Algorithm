import sys
input = sys.stdin.readline

dp = [1]*(1000001)

s = [0]*(len(dp))

for i in range(2, len(dp)):
    j = 1
    while i*j <= len(dp)-1:
        dp[i*j] += i
        j += 1
        
for i in range(1, len(dp)):
    s[i] = s[i-1] + dp[i]
    
for _ in range(int(input())):
    print(s[int(input())])