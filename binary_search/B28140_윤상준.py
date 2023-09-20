import bisect
n, q = map(int, input().split())
query = list(input())
red = []
blue = []
info = []
for _ in range(q):
    left, right = map(int, input().split())
    info.append([left, right])
for idx, que in enumerate(query):
    if que == 'R':
        red.append(idx)
    elif que == 'B':
        blue.append(idx)
for _ in range(q):
    left, right = info[_]
    rlen, blen = len(red), len(blue)
    rstart = bisect.bisect_left(red, left)
    rend = bisect.bisect_right(red, right)
    bstart = bisect.bisect_left(blue, left)
    bend = bisect.bisect_right(blue, right)
    if rend - rstart < 2 or bend - bstart < 2 or rlen < 2 or blen < 2:
        print(-1)
        continue
    elif red[rstart+1] >= blue[bend-2]:
        print(-1)
        continue
    else:
        print(red[rstart], red[rstart+1], blue[bend - 2], blue[bend-1])
