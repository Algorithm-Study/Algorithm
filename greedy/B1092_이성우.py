import sys
input = sys.stdin.readline

n = int(input().rstrip())
crain = list(map(int, input().split()))
m = int(input().rstrip())
boxes = list(map(int, input().split()))

crain.sort(reverse=True)
boxes.sort(reverse=True)
if crain[0] < boxes[0]:
    print(-1)
    exit()

answer = 0
while len(boxes) > 0:
    for c in crain:
        if boxes and boxes[-1] > c:
            continue
        for b in boxes:
            if c >= b:
                boxes.remove(b)
                break

    answer += 1

print(answer)
