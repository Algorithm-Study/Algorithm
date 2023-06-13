import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

total = 0
remainder = [0]*m

for i in range(n):
    total += arr[i]
    remainder[total%m] += 1
    
answer = remainder[0]

for i in remainder:
    answer += i*(i-1)//2
    
print(answer)