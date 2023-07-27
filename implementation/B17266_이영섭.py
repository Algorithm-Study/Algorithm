N = int(input())
M = int(input())
light = list(map(int, input().split()))
first = float(light[0])
last = float(N - light[-1])
val = 0
for i in range(M-1):
    tp = (light[i] - light[i-1])
    if tp % 2 == 0:
        tp = tp // 2
    else:
        tp = (tp // 2) + 1

    val = max(val, tp)

print(int(max(first, last, val)))
