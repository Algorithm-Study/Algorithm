import sys
import heapq
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    max_h, min_h = [], []
    visit = [False] * 1000001
    for j in range(k):
        op, num = map(str, input().split())
        num = int(num)
        if op == 'I':
            heapq.heappush(min_h, (num, j))
            heapq.heappush(max_h, (num *-1, j))
            visit[j] = True
            #print(data)
        else:
            if num == -1:
                while min_h and not visit[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visit[min_h[0][1]] = False
                    heapq.heappop(min_h)
            else:
                while max_h and not visit[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visit[max_h[0][1]] = False
                    heapq.heappop(max_h)
    while min_h and not visit[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visit[max_h[0][1]]:
        heapq.heappop(max_h)
    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')
