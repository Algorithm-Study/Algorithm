import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input().rstrip())
animals = [0]*(n+1)
graphs = [[] for _ in range(n+1)]
for i in range(2,n+1):
    species, num, connected = input().split()
    num = int(num)
    connected = int(connected)
    graphs[connected].append(i)
    # 늑대면 음수, 양이면 양수
    if species == 'W':
        animals[i] -= num
    else:
        animals[i] += num

def dfs(node):
    total = 0
    for g in graphs[node]:
        total += dfs(g)
    total = max(0, total + animals[node])
    return total
total = dfs(1)
print(total)
# 입력이 커서 Recursion error 발생 주의
# 너무 많은 리스트를 선언하면 메모리 초과