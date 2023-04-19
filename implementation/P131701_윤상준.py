def solution(elements):
    choices = elements + elements
    # 길이 1인 경우 미리 포함
    cases = set(elements)
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            cases.add(sum(choices[j:j+i]))
    return len(cases)

#Refactoring -> 테스트20 4225.22ms -> 263.60ms
def solution(elements):
    choices = elements + elements
    # 길이 1인 경우 미리 포함
    cases = set(elements)
    for i in range(1,len(elements)+1):
        total = sum(choices[0:0+i])
        cases.add(total)
        for j in range(1,len(elements)):
            total = total - choices[j-1] + choices[j+i-1]
            cases.add(total)
    return len(cases)