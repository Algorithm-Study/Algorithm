from collections import deque


def make_list(idx):
    if idx == cand[-1]:
        bf.append(new_list[:])
        return

    make_list(idx + 2)
    if idx not in new_list:
        new_list.append(idx + 2)
        make_list(idx + 2)
        new_list.pop()


def cal(a, oper, b):
    if oper == '+':
        return str(int(a) + int(b))
    elif oper == '-':
        return str(int(a) - int(b))
    elif oper == '*':
        return str(int(a) * int(b))


N = int(input())
expr = list(input())
if N == 1:
    print(int(expr[0]))
    exit()
cand = [i for i in range(0, N-1, 2)]
bf, new_list = [], []

make_list(0)
new_list.append(0)
make_list(0)

ans = -float('inf')
for case in bf:
    flag = 0
    new_expr = deque()

    for idx in range(N):
        if flag:
            flag -= 1
            continue
        if idx in case:
            new_expr.append(cal(expr[idx], expr[idx+1], expr[idx+2]))
            flag = 2
        else:
            new_expr.append(expr[idx])

    while len(new_expr) >= 3:
        tp = cal(new_expr[0], new_expr[1], new_expr[2])
        for _ in range(3):
            new_expr.popleft()
        new_expr.appendleft(tp)
    if int(tp) > ans:
        ans = int(tp)

print(ans)
