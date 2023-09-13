total = 0
line = list(input())
stack = []
temp = 1
for idx,l in enumerate(line):
    if l == '(':
        temp *= 2
        stack.append(l)
    elif l == '[':
        temp *= 3
        stack.append(l)
    elif l == ')':
        if not stack or stack[-1] ==  '[':
            print(0)
            exit()
        if line[idx-1] == '(':
            total += temp
        temp //=2
        stack.pop()
    else:
        if not stack or stack[-1] ==  '(':
            print(0)
            exit()
        if line[idx-1] == '[':
            total += temp
        temp //=3
        stack.pop()
print(total if not stack else 0)
# 괄호 조건을 충족할 때 값을 계산하는 것이 아니라 괄호 시작하면 값을 계산해야 함