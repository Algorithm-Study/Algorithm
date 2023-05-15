from collections import deque
n, k = map(int, input().split())
num = deque(input().rstrip())
answer = []

while num:
    answer.append(num.popleft())
    while (answer != []) and num and (int(answer[-1]) < int(num[0]) and k > 0):
        answer.pop()
        k -= 1
for _ in range(k):
    answer.pop()
print(''.join(answer))