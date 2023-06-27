import sys
sys.setrecursionlimit(10**7)

def dfs(x):
    global answer
    visited[x] = True
    cycle.append(x)
    number = numbers[x]

    if visited[number]:
        if number in cycle:
            answer += cycle[cycle.index(number):]
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [False]*(N+1)
    answer = []

    for i in range(1, N + 1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(N - len(answer))