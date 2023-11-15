import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

# 초기값 설정
abs_heap = []
val_dict = defaultdict(int)

# 우선순위 큐 구현
for _ in range(int(input())):
    i = int(input())
    if i != 0:
        heapq.heappush(abs_heap, abs(i))
        val_dict[i] += 1
    elif i == 0:
        if abs_heap:
            num = heapq.heappop(abs_heap)
            if val_dict[-num] >= 1:
                print(-num)
                val_dict[-num] -= 1
            else:
                print(num)
                val_dict[num] -= 1
        else:
            print(0)

# 앞에서부터 비교하고 같으면 다음 자리를 비교해서
# 우선 순위가 같으면 더 짧거나 작은 쪽이 반환된다
# 그래서 튜플로 넣고 try except로 꺼내는 방법도 있다