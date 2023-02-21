from collections import deque

n = int(input())
visit = [0 for _ in range(n)]
family = [[] for _ in range(n)]
a, b = map(int, input().split())
m = int(input())

for i in range(m):
    x, y = map(int, input().split())
    family[x-1].append(y-1)
    family[y-1].append(x-1)

queue = deque([])
for num in family[a-1]:
    queue.append(num)
    visit[num] = 1
    while len(queue) != 0:
        value = queue.popleft()
        for val in family[value]:
            if visit[val] != 0:
                continue
            queue.append(val)
            visit[val] = visit[value] + 1


if visit[b-1] == 0:
    print(-1)
else:
    print(visit[b-1])