N, M = map(int, input().split())
A = [0] + list(map(int, input().split())) #byte
C = [0] + list(map(int, input().split())) #cost
dp = [[0 for _ in range(sum(C)+1)] for _ in range(N+1)] #냅색알고리즘이 실행될 dp
result = sum(C) #열의 최댓값

for i in range(1, N+1):
    byte = A[i]
    cost = C[i]
    
    for j in range(0, sum(C) + 1):
        if j < cost: #현재 앱을 비활성화할만큼의 cost가 충분하지 않을 경우
            dp[i][j] = dp[i-1][j]
        else:
        	#같은 cost 내에서 현재 앱을 끈 뒤의 byte와 현재 앱을 끄지 않은 뒤의 byte를 비교
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
            
        if dp[i][j] >= M: #조건이 충족된다면
            result = min(result, j) #더 작은 cost값으로 갱신

print(result)

# ref : https://claude-u.tistory.com/445