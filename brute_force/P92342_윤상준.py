#무조건 1개 차이로 더 많이 맞추거나 아예 맞추지 말아야 함
def solution(n, info):
    apeach_score = sum([idx for idx, _ in enumerate(info[::-1]) if _ > 0])
    answer = [-1]
    trial = 0 
    final_gap = -56
    while trial != 11:
        i = n
        ryan_shoot = [0]*11
        ryan_score = 0
        score = apeach_score
        for pos in range(trial,11):
            if info[pos] + 1 > i:
                if pos != 10:
                    continue
                else:
                    ryan_shoot[pos] = i
                    i = 0
                    break
            else:
                ryan_shoot[pos] = info[pos] + 1
                i -= info[pos] + 1
                ryan_score += 10 - pos
                if info[pos] != 0:
                    score -= 10 - pos
        gap = ryan_score - score
        print(ryan_shoot)
        print(gap)
        if gap > final_gap:
            final_gap = gap
            if final_gap > 0:
                answer =ryan_shoot
        elif gap == final_gap and final_gap > 0:
            for j in range(10,-1,-1):
                print(j)
                if answer[j] > ryan_shoot[j]:
                    break
                answer =ryan_shoot
        trial += 1 
    return answer
#위 방식으로는 해결 불가 모든 케이스를 생각해야 함

from itertools import product
def solution(n, info):
    answer = [-1]
    chance = [0, 1]
    cases = list(product(chance, repeat = 11))
    highest = -56
    for case in cases:
        ryan_shoot = [info[x]+1 if case[x] else 0 for x in range(11)]
        num_shoot = sum(ryan_shoot)
        if num_shoot <= n:
            apeach_score = sum([10 - x if ryan_shoot[x] <= info[x]  and info[x] != 0 else 0 for x in range(11)])
            ryan_score = sum([10-x if ryan_shoot[x] != 0 and ryan_shoot[x] > info[x] else 0 for x in range(11)])
            gap = ryan_score - apeach_score
            if gap > highest and gap > 0:
                answer = ryan_shoot
                answer[10] += n- num_shoot
                highest = gap
    return answer
    