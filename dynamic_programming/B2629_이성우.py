
n = int(input())
weight = list(map(int, input().split()))

tc = int(input())
test = list(map(int, input().split()))

dp = [False] * 40001
dp[0] = True

for w in weight:
    cnt = set()
    for i in range(40001):
        if dp[i] == True:
            if i + w <= 40001:
                cnt.add(i+w)
            cnt.add(abs(i-w))
            
    for c in cnt:
        dp[c] = True

for t in test:
    if dp[t] == True:
        print('Y', end=" ")
    else:
        print('N', end=" ")