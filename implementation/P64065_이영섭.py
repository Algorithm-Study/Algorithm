def solution(s):
    answer = []
    flag = False
    ans = []
    temp = []
    stri = ''
    for i in s[1:-1]:
        if flag:
            if i == ',':
                temp.append(int(stri))
                stri = ''
            elif i == '}':
                temp.append(int(stri))
                ans.append(temp)
                temp = []
                stri = ''
                flag = False
            else:
                stri += i
        if i == '{':
            stri = ''
            flag = True
    ans.sort(key= lambda x:len(x))
    for i in ans:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer