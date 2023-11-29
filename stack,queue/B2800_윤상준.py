from itertools import combinations
line = input()
stack = []
cases = []
for i in range(len(line)):
    if line[i] == '(':
        stack.append(i)
    elif line[i] == ')':
        cases.append((stack.pop(),i))
result = set()
for i in range(1,len(cases)+1):
    for case in combinations(cases,i):
        temp = list(line)
        for l,r in case:
            temp[l], temp[r] = '',''
        result.add(''.join(temp))
result = sorted(list(result))
for r in result:
    print(r)