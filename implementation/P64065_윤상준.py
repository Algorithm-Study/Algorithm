def solution(s):
    answer = []
    data = s[1:-1]
    tuples = []
    while data.find('}') != -1:
        start, end = data.find('{'), data.find('}')
        temp = list(map(int, data[start+1:end].split(',')))
        tuples.append(temp)
        if len(data)-1 == end:
            break
        data = data[end+2:]
    tuples.sort(key = len)
    for tuple in tuples:
        for t in tuple:
            if t not in answer:
                answer.append(t)
    return answer

# 알게 된점 -> sort에서 key로 len을 사용하면 길이 순으로 정렬 가능