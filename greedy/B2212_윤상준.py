n = int(input())
k = int(input())
if n <=k:
    print(0)
    exit(0)
sensors = sorted(list(map(int, input().split())))
dist = []
for i in range(1,n):
    dist.append(sensors[i]-sensors[i-1])
dist.sort()
for i in range(k-1):
    dist.pop()
print(sum(dist))
# 전체 거리 중 큰 순서대로 k-1개 제거 후 남은 거리의 총합 구하면 끝
# 센서 수보다 집중국이 더 많은 경우가 존재해서 예외 처리 필요