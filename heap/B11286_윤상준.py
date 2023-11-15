#python의 경우 최소힙으로 구현되어 있음
#입력값이 최대 2^31 이므로 입력을 빠르게 받아서 처리해야 함!
import heapq
import sys
input = sys.stdin.readline
n = int(input().rstrip())
p_heap = []
n_heap = []
for _ in range(n):
    op = int(input().rstrip())
    #절댓값 출력
    if op == 0:
        if len(p_heap) == 0 and len(n_heap) == 0:
            print(0)
        elif len(p_heap) == 0 and len(n_heap) != 0:
            n_min = heapq.heappop(n_heap)
            print(-n_min)
        elif len(p_heap) != 0 and len(n_heap) == 0:
            p_min = heapq.heappop(p_heap)
            print(p_min)
        else:
            p_min = heapq.heappop(p_heap)
            n_min = heapq.heappop(n_heap)
            if p_min >= n_min:
                print(-n_min)
                heapq.heappush(p_heap, p_min)
            else:
                print(p_min)
                heapq.heappush(n_heap, n_min)
    else:
        if op >= 0:
            heapq.heappush(p_heap, op)
        else:
            heapq.heappush(n_heap, op* -1)

#파이썬의 기본 heap은 최소합이기 때문에 최대힙과 최소합의 구현을 할 수 있다는 점을 활용
#음수 저장 힙과 양수 저장 힙으로 나누어서 저장하는 것을 통해 문제 해결

#======New Code======
import sys, heapq

queue = []
n = int(sys.stdin.readline())
for i in range(n):
	num = int(sys.stdin.readline())
	if num:
		heapq.heappush(queue, (abs(num), num))
	else:
		if queue:
			print(heapq.heappop(queue)[1])
		else:
			print(0)       