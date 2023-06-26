def solution(s):
    answer = 1
    
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 2
            answer = 2
    
    for j in range(2, len(s)):
        for i in range(len(s)-j):
            if dp[i+1][i+j-1] != 0 and s[i:i+j+1] == s[i:i+j+1][::-1]:
                dp[i][i+j] = dp[i+1][i+j-1] + 2
                answer = max(answer, j+1)
    

    return answer
