from itertools import permutations
def solution(expression):
    answer = 0
    cases = list(permutations(['*', '+', '-'], 3))
    print(cases)
    arith = []
    num = []
    temp = ''
    for ex in expression:
        if ex.isdigit():
            temp += ex
        else:
            num.append(temp)
            temp = ''
            arith.append(ex)
    num.append(temp)
    for case in cases:
        symbols = arith[:]
        numbers = [int(x) for x in num]
        for c in case:
            stack_ar = []
            stack_num = [numbers[0]]
            for j in range(len(symbols)):
                stack_num.append(numbers[j+1])
                stack_ar.append(symbols[j])
                if stack_ar[-1] == c:
                    x1,x2 = stack_num.pop(), stack_num.pop()
                    symbol = stack_ar.pop()
                    if symbol == '*':
                        stack_num.append(x1 * x2)
                    if symbol == '+':
                        stack_num.append(x1 + x2)
                    if symbol == '-':
                        stack_num.append(x2 - x1)
            numbers = stack_num
            symbols = stack_ar
        answer = max(answer, abs(numbers[0]))
        #print(answer)
    return answer
# 스택으로 우선순위 연산자를 만난 경우 연산 후 다시 스택에 넣는 방식으로 해결