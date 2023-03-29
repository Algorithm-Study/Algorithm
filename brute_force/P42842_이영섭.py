def solution(brown, yellow):
    answer = []
    whole = brown + yellow
    for i in range(whole//2, 0, -1):
        if whole % i  == 0 and i*2 + (whole//i-2)*2 == brown:
            answer.append(i)
            answer.append(whole//i)
            break
    return answer