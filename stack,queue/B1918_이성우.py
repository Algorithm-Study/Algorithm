expression = list(input())
stack = []
answer = ''
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
for s in expression:
    if s.isalpha(): # 피연산자 바로 출력
        answer += s
    elif s == '(': # 여는 괄호면 스택에 푸시
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(': # 닫는 괄호면 여는 괄호까지 스택 팝
            answer += stack.pop()
        stack.pop()
    else:
        # 스택에 있는 연산자 중 현재보다 우선순위가 높거나 같은 것들은 팝하고 출력
        while stack and stack[-1] != '(' and priority[stack[-1]] >= priority[s]:
            answer += stack.pop()
        stack.append(s)
        
# 남은 연산자 출력
while stack:
    answer += stack.pop()
    
print(answer)