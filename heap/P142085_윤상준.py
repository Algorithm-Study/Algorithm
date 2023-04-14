# 재귀함수로 로직 구현하면 런타임 에러 -> python recursion limit에 걸리는 것으로 예상
import heapq
def solution(n, k, enemy):
    answer = 0
    wave = enemy[:k]
    heapq.heapify(wave)
    for i in range(k,len(enemy)):
        heapq.heappush(wave, enemy[i])
        n -= heapq.heappop(wave)
        if n < 0:
            return i
    return len(enemy)