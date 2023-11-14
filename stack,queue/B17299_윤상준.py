n = int(input())
data = list(map(int, input().split()))
counter = [0]*1_000_001
stack = []
result = [-1]*n
for c in data:
    counter[c] += 1
for i in range(n):
    while stack and counter[data[stack[-1]]] < counter[data[i]]:
        result[stack.pop()] = data[i]
    stack.append(i)
print(*result)