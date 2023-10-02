st = list(input())
stack = []
oper = ['+', '-', '*', '/', '(', ')']
ans = ''
for s in st:
    if s not in oper:
        ans += s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()

while stack:
    ans += stack.pop()
print(ans)
