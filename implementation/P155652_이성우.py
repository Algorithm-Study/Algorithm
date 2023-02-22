def solution(s, skip, index):
    alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    answer = ''
    
    for i in skip:
        alp.remove(i)

    for i in s:
        answer += alp[(alp.index(i)+index)%len(alp)]

    return answer