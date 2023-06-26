import sys
sys.setrecursionlimit(10**5)

def dfs(pick,cycle):
    global teams
    cycle.append(pick)
    visited[pick] = 1
    if visited[picks[pick]]:
        if picks[pick] in cycle:
            teams += cycle[cycle.index(picks[pick]):]
        return   
    else:
        dfs(picks[pick],cycle)
        
t = int(input())
for _ in range(t):
    n = int(input())
    teams = []
    picks = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    for i in range(1,n+1):
        if visited[i] == 0:
            dfs(i, [])
    print(n-len(teams))
# 사이클 형성 문제
# set recrusion limit을 너무 크게 하면 메모리 초과 
# 완전 사이클을 구하는 방식으로는 시간 초과
# 방문 처리하지 않으면 시간 초과
# => python으로 시간 엄청 빡빡한 문제
