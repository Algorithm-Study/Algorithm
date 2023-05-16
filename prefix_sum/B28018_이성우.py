import sys
input = sys.stdin.readline

arr = [0]*1_000_002
for _ in range(int(input().rstrip())):
    start, end = map(int, input().split())
    arr[start] += 1
    arr[end+1] += -1
    
for idx in range(1,1_000_002):
    arr[idx] += arr[idx-1]
    
n = input()

print(*[arr[i] for i in list(map(int, input().split()))], sep='\n')