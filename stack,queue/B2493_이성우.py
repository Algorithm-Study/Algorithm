n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = [0] * n

for idx in range(n):
    t = arr[idx]
    while stack and arr[stack[-1]] < t:
        stack.pop()
    if stack:
        answer[idx] = stack[-1] + 1
    stack.append(idx)

print(*answer)
