import heapq
import sys
input = sys.stdin.readline
n = int(input())
lqueue = []
rqueue = []
llen, rlen = 0,0
for i in range(1,n+1):
    if llen == rlen:
        heapq.heappush(lqueue,-int(input()))
        llen += 1
    else:
        heapq.heappush(rqueue,int(input()))
        rlen += 1
    # 좌측 최대값이 우측 최솟갑보다 큰 경우(Swap)
    if rlen > 0 and -lqueue[0] > rqueue[0]:
        t1, t2 = -heapq.heappop(lqueue), heapq.heappop(rqueue)
        heapq.heappush(rqueue, t1)
        heapq.heappush(lqueue, -t2)
    print(-lqueue[0])
# 중간 값을 기준으로 두 개의 힙안에 값을 저장하면 문제해결 가능