N = int(input())
A = list(map(int, input().split()))
cache = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            cache[i] = max(cache[i], cache[j]+1)

print(max(cache))
