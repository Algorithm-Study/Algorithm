# 가능한 알파벳 리스트 생성 후 암호로 해독
def solution(s, skip, index):
    order = [chr(x) for x in range(ord('a'), ord('z')+1)]
    for sk in list(skip):
        order.remove(sk)
    answer = ''
    for alpha in list(s):
        answer += order[(order.index(alpha)+index)%len(order)]
    return answer