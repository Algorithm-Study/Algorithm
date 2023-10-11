import heapq

t = int(input())
for _ in range(t):
    max_heap, min_heap = [], []
    visit = [0] * 1_000_001

    k = int(input())

    for key in range(k):
        st, n = input().split()
        if st == 'I':
            heapq.heappush(min_heap, (int(n), key))
            heapq.heappush(max_heap, (int(n) * -1, key))
            visit[key] = True
        elif n == '-1':
            while min_heap and not visit[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visit[min_heap[0][1]] = False
                heapq.heappop(min_heap)
        elif n == '1':
            while max_heap and not visit[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visit[max_heap[0][1]] = False
                heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
