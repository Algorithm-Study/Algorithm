def solution(elements):
    choices = elements + elements
    # 길이 1인 경우 미리 포함
    cases = set(elements)
    for i in range(1,len(elements)+1):
        for j in range(len(elements)):
            cases.add(sum(choices[j:j+i]))
    return len(cases)