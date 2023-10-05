import bisect
n = int(input())
cranes = list(map(int, input().split()))
cranes.sort()
todo = [0]*n
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse = True)

for box in boxes:
    idx = bisect.bisect_left(cranes, box)
    if box > cranes[-1]:
        print(-1)
        exit()
    val = min(todo[idx: n])
    for i in range(n-1, idx-1, -1):
        if todo[i] == val:
            todo[i] += 1
            break
print(max(todo))