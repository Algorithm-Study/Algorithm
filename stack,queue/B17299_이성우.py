from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
d = Counter(arr)
answer = [-1]*n
stack = [0]

for i in range(1, n):
    while stack and d[arr[stack[-1]]] < d[arr[i]]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)