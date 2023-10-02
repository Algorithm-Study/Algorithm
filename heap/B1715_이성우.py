import heapq, sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    num = int(input().rstrip())
    heapq.heappush(arr, num)
    
answer = 0

while len(arr) != 1:
    num1, num2 = heapq.heappop(arr), heapq.heappop(arr)
    num3 = num1 + num2
    answer += num3
    if arr:
        heapq.heappush(arr, num3)
    else:
        break
print(answer)