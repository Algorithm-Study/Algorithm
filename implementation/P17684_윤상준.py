def solution(msg):
    LZW = {}
    for i in range(ord('A'),ord('Z')+1):
        LZW[chr(i)] = i - ord('A')+ 1
    answer = []
    list_msg = list(msg)
    iscontain = ''
    while len(list_msg) > 0:
        iscontain += list_msg.pop(0)
        if len(list_msg) != 0:
            if (iscontain + list_msg[0]) not in LZW:
                answer.append(LZW[iscontain])
                LZW[iscontain + list_msg[0]] = len(LZW)+1
                iscontain = ''
        #맨 마지막에 하나 남은 경우 예외 처리
        else:
            answer.append(LZW[iscontain])
            break
    
    return answer