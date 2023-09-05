n = int(input())
s = input()
answer = -float('inf')

def cal(num1, oper, num2):
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2

def dfs(index, value):
    global answer
    if index == n - 1:
        answer = max(answer, int(value))
        return

    if index + 2 < n:
        dfs(index + 2, cal(value, s[index + 1], int(s[index + 2])))

    if index + 4 < n:
        dfs(index + 4, cal(value, s[index + 1], cal(int(s[index + 2]), s[index + 3], int(s[index + 4]))))

dfs(0, int(s[0]))
print(answer)