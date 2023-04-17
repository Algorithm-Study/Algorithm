n = int(input())
stairs = [int(input()) for _ in range(n)]
total = [0 for _ in range(n)]
if n <= 2:
    print(sum(stairs))
else:
    total[0] = stairs[0]
    total[1] = stairs[0] + stairs[1]
    for i in range(2, n):
        total[i] = max(total[i-3] + stairs[i-1] + stairs[i], total[i-2] + stairs[i])
    print(total[-1])