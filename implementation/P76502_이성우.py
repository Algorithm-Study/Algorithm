def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        new_s = s
        for _ in range(len(new_s)//2):
            new_s = new_s.replace('[]','')
            new_s = new_s.replace('{}','')
            new_s = new_s.replace('()','')
        if new_s == '':
            answer += 1
    return answer