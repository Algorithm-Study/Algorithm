import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
target = sum(arr[:])
answer = 0
temp = 0

for i in range(1, n):
    temp += arr[i]
    answer = max(answer, target - arr[0] - arr[i] + target - arr[0] - temp)

arr.reverse()
temp = 0  
for i in range(1, n):
    temp += arr[i]
    answer = max(answer, target - arr[0] - arr[i] + target - arr[0] - temp)

for i in range(1, n):
    answer = max(answer, target - arr[0] - arr[-1] + arr[i])

print(answer)
