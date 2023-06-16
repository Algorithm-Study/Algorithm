import heapq
n = int(input())
task = []
max_day = 0
for _ in range(n):
    day, point = map(int, input().split())
    max_day = max(max_day, day)
    task.append((day, point))
task.sort(key= lambda x : [x[0], x[1]])

h = []
days = [0]*(max_day+1)
for d in range(max_day+1)[::-1]:
    while task:
        day, point = task.pop()
        if day < d:
            task.append((day, point))
            break
        else:
            heapq.heappush(h, (-point, day))
    if h:
        point, day = heapq.heappop(h) # point 음수
        days[d] = -point

print(sum(days[1:]))