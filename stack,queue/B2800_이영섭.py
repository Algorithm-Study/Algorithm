from itertools import combinations

equation = list(input())
st = []
bracket = []
for idx, e in enumerate(equation):
    if e == '(':
        st.append(idx)
    elif e == ')':
        bracket.append((st.pop(), idx))

ans = set()
for i in range(len(bracket)):
    bf = list(combinations(bracket, r=i+1))
    for case in bf:
        out_char, in_string = {}, ""
        for c1, c2 in case:
            out_char[c1] = 1
            out_char[c2] = 1
        for idx, e in enumerate(equation):
            if idx not in out_char:
                in_string += e
        ans.add(in_string)

ans = sorted(list(ans))
for a in ans:
    print(a)
