import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    max_h = []
    min_h = []
    visited = [False]*1_000_001

    for key in range(n):
        c, num = input().split()
        num = int(num)
        if c == 'I':
            heapq.heappush(max_h, (-num, key))
            heapq.heappush(min_h, (num, key))
            visited[key] = True
            
        elif c == 'D':
            if num == 1:
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            elif num == -1:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)
    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
            
    if max_h and min_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print('EMPTY')