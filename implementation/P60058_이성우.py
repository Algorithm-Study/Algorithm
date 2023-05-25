from typing import Tuple
def solution(p):
    def seperate(p: str) -> Tuple[str, str]:
        '''
        입력 문자열을 두 균형잡힌 괄호 문자열 u, v로 반환
        단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없고
        v는 빈 문자열도 가능
        '''
        cnt_open = 0
        cnt_close = 0
        for i in range(len(p)):
            if p[i] == '(':
                cnt_open += 1
            else:
                cnt_close += 1
            if cnt_open == cnt_close:
                return p[:i+1], p[i+1:]
            
    def is_right_braket(letters: str) -> bool:
        '''
        올바른 괄호 문자열인지 확인
        '''
        arr = list(letters)
        tmp = []
        while arr:
            braket = arr.pop()
            if tmp and braket + tmp[-1] == '()':
                tmp.pop()
            else:
                tmp.append(braket)
        if tmp == []:
            return True
        else:
            return False
        
    def sol(letters: str) -> str:
        '''
        올바른 괄호 문자열로 변환
        '''
        if is_right_braket(letters):
            return letters
        else:
            u, v = seperate(letters)
            if is_right_braket(u):
                u += sol(v)
                return u
            else:
                tmp = '('
                tmp += sol(v) + ')'
                for i in range(1,len(u)-1):
                    if u[i] == '(':
                        tmp += ')'
                    else:
                        tmp += '('
                return tmp
    
    return sol(p)