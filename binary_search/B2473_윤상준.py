n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
abs_min = 3_000_000_001
answer = [0, 0]
for _ in range(n-2):
    mid = liquids.pop()
    start, end = 0, len(liquids) - 1
    while start < end:
        if liquids[start] + liquids[end] + mid == 0:
            print(liquids[start], liquids[end], mid)
            exit(0)
        if liquids[start] + liquids[end] + mid < 0:
            if abs(liquids[start] + liquids[end] + mid) < abs_min:
                answer = [liquids[start], liquids[end], mid]
                abs_min = abs(liquids[start] + liquids[end] + mid)
            start += 1
        else:
            if abs(liquids[start] + liquids[end] + mid) < abs_min:
                answer = [liquids[start], liquids[end], mid]
                abs_min = abs(liquids[start] + liquids[end] + mid)
            end -= 1
print(answer[0], answer[1], answer[2])