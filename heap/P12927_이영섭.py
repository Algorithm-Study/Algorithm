import heapq

def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heapq.heappush(heap, -i)
    for _ in range(n):
        if len(heap) <= 0:
            break
        out = heapq.heappop(heap)
        if out < 0:
            heapq.heappush(heap, out+1)
    for hp in heap:
        answer += hp ** 2
    return answer

# 문제 접근 방법
# # 배열 간 차이를 가장 적게 해줘야 함
# # 최대 힙을 이용해 간단하게 해결 가능