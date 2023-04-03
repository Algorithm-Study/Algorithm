S = input()
T = input()
answer = 0

def dfs(t):
    global answer
    if t == S:
        answer = 1
        return
    if len(t) == 0:
        return
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[:0:-1])
        
dfs(T)
print(answer)

# 완전탐색으로 풀다가 시간초과