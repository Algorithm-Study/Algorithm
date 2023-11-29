from itertools import combinations

# 변수 초기화
string = list(input())
answer = set()
stack = []
tmp = []

# 괄호쌍 인덱스 수집
for idx, word in enumerate(string):
    if word == '(':
        stack.append(idx)
    elif word == ')':
        tmp.append((stack.pop(), idx))
        
# 괄호쌍 인덱스 제거 케이스
for i in range(1, len(tmp) + 1):
    cases = combinations(tmp, i)
    # 케이스에서 괄호 제거
    for c in cases:
        target = string[:]
        for k in c:
            target[k[0]] = ''
            target[k[1]] = ''
        answer.add(''.join(target))
       
# 정렬 후 출력 
for ans in sorted(answer):
    print(ans)