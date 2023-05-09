def solution(n, s):
    # 초기 변수값
    answer = []
    
    # n이 더 커서 나눌 수 없으면 [-1] 반환
    if n > s:
        return [-1]
    else:
        # 공평하게 나누어지게 계산
        while n:
            num = s//n
            answer.append(num)
            n -= 1
            s -= num
        return answer