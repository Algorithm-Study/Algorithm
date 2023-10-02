equation = list(input())
result = ''
stack = []
for eq in equation:
    if eq.isalpha():
        result += eq
    else:
        # 괄호를 만난 경우
        if eq == '(':
            stack.append(eq)
        # +- 인 경우
        elif eq == '+' or eq == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(eq)
        elif eq == '*' or eq == '/':
            while stack and stack[-1] in ['*','/']:
                result += stack.pop()
            stack.append(eq)
        else:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)