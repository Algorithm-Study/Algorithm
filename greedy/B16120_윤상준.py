line = list(input())
stack = []
for l in line:
    stack.append(l)
    if stack[-4:] == ['P','P','A','P']:
        for i in range(4):
            stack.pop()
        stack.append('P')
if stack == ['P','P','A','P'] or stack == ['P']:
    print('PPAP')
else:
    print('NP')
# 슬라이싱으로 진행하면 문제해결 불가능
# pop을 활용해야 해결 가능