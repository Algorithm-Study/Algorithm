n, d = map(int, input().split())
pos = [x for x in range(10001)]
route = sorted(list(map(int,input().split())) for _ in range(n))
for i in range(n):
    start, end, dist = route[i]
    pos[end] = min(pos[end], pos[start]+dist)
    for j in range(d):   
        pos[j+1] = min(pos[j]+1, pos[j+1])
print(pos[d])
#다익스트라보다는 dp로 푸는 것도 가능
#0에서 가장 가까운 지름길부터 체크해야 최단 거리 구하기 가능