def solution(lottos, win_nums):
    zero =lottos.count(0)
    cnt = 0
    win_rate = [6,6,5,4,3,2,1]
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    answer = [win_rate[cnt+zero],win_rate[cnt]]
    return answer