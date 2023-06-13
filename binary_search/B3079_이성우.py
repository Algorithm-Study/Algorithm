import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

left, right = min(arr), max(arr)*m
answer = right


while left <= right:
    total = 0
    mid = (left + right)//2
    
    for i in range(n):
        total += mid // arr[i]
        
    if total >= m:
        right = mid - 1
        answer = min(mid, answer)    

    else:
        left = mid + 1
        
print(answer)