def solution(s, skip, index):
    answer = ''
    s_list = []
    non_skip_list = [chr(ord) for ord in range(ord('a'), ord('z')+1) if chr(ord) not in skip]

    for i in range(len(s)):
        s_list.append(s[i])
        
    for i in range(len(s_list)):
        answer += non_skip_list[(non_skip_list.index(s_list[i]) + index) % len(non_skip_list)]

    return answer