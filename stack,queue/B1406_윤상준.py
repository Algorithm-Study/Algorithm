import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
m = int(input())
for _ in range(m):
    op = list(input().split())
    if op[0] == 'L':
        if len(left) == 0:
            continue
        temp = left.pop()
        right.append(temp)
    elif op[0] == 'D':
        if len(right) == 0:
            continue
        temp = right.pop()
        left.append(temp)
    elif op[0] == 'B':
        if len(left) == 0:
            continue
        left.pop()
    else:
        left.append(op[1])
    #print(left, right)
result = left + list(reversed(right))
print(''.join(result))

# stack으로 시간 복잡도를 줄여도 sys를 사용하지 않으면 시간초과 발생