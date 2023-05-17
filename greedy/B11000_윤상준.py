import heapq
n = int(input())
start = []
end = []
for _ in range(n):
    s, e = map(int, input().split())
    heapq.heappush(start, s)
    heapq.heappush(end, e)
cs = heapq.heappop(start)
ce = heapq.heappop(end)
count = 0
max_val = 0
while start:
    if cs > ce:
        ce = heapq.heappop(end)
        count -= 1
    elif cs == ce:
        ce = heapq.heappop(end)
        cs = heapq.heappop(start)
    else:
        cs = heapq.heappop(start)
        count += 1
    max_val = max(max_val, count)
print(max_val)

# 시작 시간과 종료 시간 별도의 힙을 활용해서 문제 해결
# 하나의 힙으로 처리하는 방법도 있음