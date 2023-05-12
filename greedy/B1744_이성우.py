n = int(input())
pos = []
neg = []
answer = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        pos.append(num)
    elif num < 1:
        neg.append(num)
    else:
        answer += 1
pos.sort()
neg.sort(reverse=True)

tmp = 0
while pos:
    num = pos.pop()
    if tmp == 0:
        tmp = num
    else:
        answer += num*tmp
        tmp = 0
answer += tmp

tmp = 0
while neg:
    num = neg.pop()
    if tmp == 0:
        tmp = num
    else:
        answer += num*tmp
        tmp = 0
answer += tmp

print(answer)
