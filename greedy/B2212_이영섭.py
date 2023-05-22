N = int(input())
K = int(input())
data = list(map(int, input().split()))
if K >= N:
    print(0)
else:
    data.sort()
    distance = [data[i+1]-data[i] for i in range(N-1)]
    distance.sort()
    for _ in range(K-1):
        distance.pop()
    print(sum(distance))
