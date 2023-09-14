string = list(input())
stack = []
temp, ans = 1, 0
last_str = ''
for s in string:
    if s == '(':
        temp *= 2
        stack.append(s)
    elif s == '[':
        temp *= 3
        stack.append(s)
    elif s == ')':
        if len(stack) == 0 or stack[-1] == '[':
            print(0)
            exit()
        stack.pop()
        if last_str == '(':
            ans += temp
        temp /= 2
    elif s == ']':
        if len(stack) == 0 or stack[-1] == '(':
            print(0)
            exit()
        stack.pop()
        if last_str == '[':
            ans += temp
        temp /= 3
    last_str = s

if len(stack) != 0:
    print(0)
    exit()
print(int(ans))
