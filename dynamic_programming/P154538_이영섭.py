from collections import deque
def solution(x, y, n):
    answer = -1
    inf = 1000001
    arr = [inf] * inf * 3
    num = deque()
    if x == y:
        return 0
    for ys in [x+n, 2*x, 3*x]:
        if ys <= y: num.append(ys)
        arr[ys] = 1
    while num:
        val = num.popleft()
        for ys in [val+n, 2*val, 3*val]:
            if ys <= y and arr[ys] == inf:
                num.append(ys)
                arr[ys] = min(arr[ys], arr[val] + 1)
            else:
                continue
    answer = arr[y]
    if arr[y] == inf:
        answer = -1
    return answer