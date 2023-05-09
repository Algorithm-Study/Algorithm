import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    while n != 0:
        temp = heapq.heappop(works)
        if temp != 0:
            temp += 1
        heapq.heappush(works, temp)
        n -= 1
    return sum([x**2 for x in works])

# heapq 활용해서 최대힙 생성 후 heappop으로 나오는 값들에서 0인 경우를 제외하고 1씩 증가시킴
# 이후 제곱합을 구해서 return 하면 통과