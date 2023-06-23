N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
stack = []
answer = 0

arr.append([0, 0])

for x, y in arr:
    while stack and stack[-1] >= y:  
        if stack.pop() > y:
            answer += 1

    stack.append(y)

print(answer)
