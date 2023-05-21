def solution(str1, str2):
    answer = 0
    jip1, jip2 = [], []
    for idx, i in enumerate(str1[1:]):
        if str1[idx].isalpha() and i.isalpha():
            jip1.append((str1[idx]+i).lower())
    for idx, i in enumerate(str2[1:]):
        if str2[idx].isalpha() and i.isalpha():
            jip2.append((str2[idx]+i).lower())
    if len(jip1) + len(jip2) == 0:
        return 65536
    result = []
    tmp = jip2[:]
    for i in jip1:
        if i in tmp:
            tmp.remove(i)
            result.append(i)
    union = len(jip1) + len(jip2) - len(result)

    if (len(jip1) == 0 and len(jip2) == 0):
        answer = 1
    else:
        answer = len(result)/union
    return int(65536 * answer)