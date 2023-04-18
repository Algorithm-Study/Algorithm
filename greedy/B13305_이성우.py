from collections import deque
n = int(input())
roads = list(map(int,input().split()))
cities = deque(map(int,input().split()))

dq = deque()
min_val = float('inf')

answer = 0
while True:
    ref = cities.popleft()
    if len(cities) == 0:
        break
        
    if min_val >= ref:
        dq.append(ref)
        min_val = ref
    else:
        dq.append(min_val)
# print(dq)

answer = sum(road*city for road, city in zip(roads, dq))
    
print(answer)

'''
5
2 2 3 3 
5 2 3 3 1
>> 5 2 2 2
'''
    