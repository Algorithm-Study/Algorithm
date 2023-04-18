import heapq
n = int(input())
data = list(map(int, input().split()))
data = data[::-1]
stack = [data[0]]
result = [-1]
for d in data[1:]:
    flag = 0
    while stack:
        if d < stack[-1]:
            result.append(stack[-1])
            flag = 1
            break
        else:
            stack.pop()
    if flag == 0:
        result.append(-1)
    stack.append(d)

result = result[::-1]
for r in result:
    print(r, end = ' ')
        