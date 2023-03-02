def solution(msg):
    answer = []
    msg_str = msg
    # 알파벳에 해당하는 사전 선언
    dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
    # msg_str을 비어있지 않은 동안 반복
    while msg_str != '':
        w = ''
        idx = 0
        # msg_str을 앞에서 부터 보면서 사전에 들어있는 가장 긴 문자열 찾기
        for i in range(len(msg_str)):
            idx += 1
            w += msg_str[i]
            # 들어 있지 않은 것을 발견하면
            if w not in dict:
                answer.append(dict[w[:-1]]) # 이전 까지의 문자열은 출력
                dict[w] = len(dict) + 1 # 지금 문자열은 사전에 등록
                idx -= 1 # idx를 1부터 시작했으니까 -1
                break
            # 문자열의 마지막이라면 지금까지 모은 문자열을 출력(무조건 등록된 문자열)
            if i == len(msg_str) - 1:
                answer.append(dict[w])
        msg_str = msg_str[idx:]
        
    return answer

# 문제 접근 방법
# # 문제의 조건대로 해결하는 구현
# 새로 배운 python
# # 없음