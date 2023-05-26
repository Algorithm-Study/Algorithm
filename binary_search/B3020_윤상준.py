import bisect
n, h = map(int, input().split())
up = [0]*(h+1)
down  = [0]*(h+1)
for i in range(1,n+1):
    temp = int(input())
    #종유석
    if i % 2 == 0:
        up[h-temp+1] += 1
    #석순
    else:
        down[temp] += 1
for i in range(1,h+1):
    up[i] += up[i-1]
for i in range(h-1,0,-1):
    down[i] += down[i+1]
result = sorted([ up[x]+down[x] for x in range(1,h+1)])
min_break = min(result)
print(min_break, bisect.bisect_right(result, min_break))
# 누적합으로 각 위치별 마주하는 석순과 종유석을 총합을 구하고 최솟값을 구함
# 이후 정렬하여 이분탐색으로 최소로 마주하는 경우의 수 찾으면 끝