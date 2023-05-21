n = int(input())
k = int(input())
arr = list(map(int ,input().split()))
arr.sort()

tmp = []
for i in range(n-1):
    tmp.append(arr[i+1] - arr[i])

tmp.sort()

print(sum(tmp[:n-k]))