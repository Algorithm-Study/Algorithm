n = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
tg_a, tg_b = map(int, input().split())
answer = []
# answer = 0 아니라 []로 준 것은 함수 안에서 answer = 변수로 넣어도 지역변수라 밖에서 다시 0으로 돌아온다
# 하지만 append로 추가해주면 answer를 변화시킬 수 있다
for i in range(int(input())):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

print(graph)

def dfs(v, num):

    num += 1
    visited[v] = True

    if v == tg_b:
        answer.append(num)
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i ,num)

dfs(tg_a, 0)
# 한 곳에서 시작해서 tg_b가 나올 때까지 찾으면 촌수를 계산할 수 있다
if len(answer) == 0:
    print(-1)
else:
    print(answer[0]-1)