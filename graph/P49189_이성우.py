from typing import List
import heapq

def solution(n: int, edge: List[int]) -> int:
    answer = 0
    arr = [[] for _ in range(n+1)]
    distance = [float('inf')]*(n+1)
    for e in edge:
        arr[e[0]].append((e[1], 1))
        arr[e[1]].append((e[0], 1))
    
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
            
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    max_num = 0
    for num in distance[1:]:
        if num > max_num:
            max_num = num
            answer = 1
        elif num == max_num:
            answer += 1
    return answer