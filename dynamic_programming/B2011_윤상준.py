decipher = [0]+list(map(int, list(input())))
dp = [0]*len(decipher)
dp[0],dp[1] = 1,1
if decipher[1] == 0:
    print(0)
    exit()
for i in range(2,len(decipher)):
    if decipher[i] != 0:
        dp[i] += dp[i-1]
    if decipher[i-1] != 0 and decipher[i-1]*10 + decipher[i] < 27:
        dp[i] += dp[i-2]
print(dp[len(decipher)-1]%1_000_000) 