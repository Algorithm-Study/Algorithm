from heapq import heappop, heapify
from sys import stdin
input = stdin.readline

def minusone(num):
    return -1*int(num)

n = int(input())
answer = []

for _ in range(n):
    arr = list(map(minusone, input().split()))
    heapify(arr)
    
    for i in range(_+1):
        answer.append(heappop(arr))
    answer.sort()
    answer = answer[:n]

print(-answer[n-1])