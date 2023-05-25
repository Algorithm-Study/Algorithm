N, D = map(int, input().split())
fast_road = [list(map(int, input().split())) for _ in range(N)]
fast_road.sort(key=lambda x: x[1])
road = [0] * 10001
for i in range(1, 10001):
    road[i] = road[i-1] + 1
    for fr in fast_road:
        if road[fr[0]] + fr[2] < road[fr[1]]:
            road[fr[1]] = road[fr[0]] + fr[2]
print(road[D])