from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
INF = 9876543210
n,m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))

def solv():
    visited = [[INF,-1] for _ in range(n+1)]
    pq = [(0,1)]
    visited[1] = [n+1,0]
    while pq:
        cost,now = heappop(pq)

        for nxt,nxt_cost in adj_list[now]:
            if visited[nxt][0] == INF or visited[nxt][1] > cost+nxt_cost:
                visited[nxt] = [now,cost+nxt_cost]
                heappush(pq,(cost+nxt_cost,nxt))

    answer = set()
    for now in range(2,n+1):
        nxt = visited[now][0]
        while nxt != n+1:
            answer.add((now,nxt))
            now = nxt
            nxt = visited[now][0]

    print(len(answer))
    for a,b in answer:
        print(a,b)
solv()