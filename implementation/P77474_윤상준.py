def solution(lottos, win_nums):
    answer = []
    correct = 0
    winning = [6,6,5,4,3,2,1]
    missing = lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            correct+=1
    answer.append(winning[correct+missing])
    answer.append(winning[correct])
    return answer