def solution(k, d):
    answer = d//k +1
    for i in range(0,d+1,k):
        answer += ((d**2 - i**2)**0.5)//k

    return answer