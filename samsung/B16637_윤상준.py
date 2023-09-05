import sys
n = int(input())
expression = list(input())
answers = []
def dfs(idx, val):
    if idx == n-1:
        answers.append(val)
        return
    # 현재 위치 뒤에 연산자, 숫자가 있는 경우
    if idx + 2 < n:
        dfs(idx+2,eval(str(val) + expression[idx+1] + expression[idx+2]))
    # 뒤 연산자에 대해 괄호가 있는 경우
    if idx + 4 < n:
        dfs(idx+4, eval(str(val) + expression[idx+1] + str(eval(expression[idx+2] + expression[idx+3] + expression[idx+4]))))
dfs(0,expression[0])
print(max(answers))
# eval로 연산 진행
# dfs로 괄호가 있는 경우 없는 경우로 나눠서 진행