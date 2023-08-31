import bisect
n = int(input())
eline = list(map(int, input().split()))
lcs = []
lcs.append(eline[0])
for i in range(1,n):
    if lcs[-1] < eline[i]:
        lcs.append(eline[i])
    else:
        sub = bisect.bisect_left(lcs,eline[i])
        lcs[sub] = eline[i]
print(n-len(lcs))
# LIS 기본 유형 문제
# 길이만 알면 되기 때문에 기록을 남길 필요가 없음