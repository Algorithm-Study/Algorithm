from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    new_list = []
    heap = []
    if len(enemy) < k:
        return len(enemy)
    for i in range(k):
        heappush(heap, enemy[i])
    for i in range(k, len(enemy)):
        heappush(heap, enemy[i])
        n -= heappop(heap)
        if n < 0:
            return i
    return len(enemy)

# 문제 접근 방법
# # 앞에 있는 것중에 '가장 작은 수를 뽑아내서' 그 값만큼 n에서 빼주면
# # k개의 큰 것들에 대해서만 무적권을 사용할 수 있음
# # heap 자료구조를 사용하여 구현하고 k가 enemy보다 큰 경우
# # 무조건 enemy개의 라운드를 통과할 수 있음(체크 안하면 런타임에러)