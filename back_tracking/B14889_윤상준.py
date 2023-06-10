from itertools import permutations
n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
result = []

def dfs(num,x):
    if num == n//2:
        start = 0
        link = 0
        for case in permutations([x for x in range(n) if visited[x] == True], 2):
            start += synergy[case[0]][case[1]]
        for case in permutations([x for x in range(n) if visited[x] == False], 2):
            link += synergy[case[0]][case[1]]
        result.append(abs(start-link))
        return
    for i in range(x,n):
        if not visited[i]:
            visited[i] = True
            dfs(num+1, i+1)
            visited[i] = False 
dfs(0,0)
print(min(result)) 

# dfs를 활용하면 풀 수 있는 문제