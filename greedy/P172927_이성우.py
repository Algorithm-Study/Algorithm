from collections import deque
from itertools import permutations as pmt

def solution(picks, minerals):
    
    # 변수 초기화
    picks_dict = {'diamond':2, 'iron':1, 'stone':0}
    PICKS = ['diamond', 'iron', "stone"]
    picks_list = []
    answer = float('inf')

    # 곡괭이 리스트 생성
    for PICK, pick in zip(PICKS,picks):
        picks_list += [PICK]*pick
    
    # 곡괭이 개수와 광물//5+1 중에 더 적은 수만큼의 곡괭이만 뽑아서 순열 생성
    for permutation in set(pmt(picks_list, min(len(picks_list),(len(minerals)//5+1)))):
        fatigue = 0
        a = 0
        
        # 곡괭이로 5개씩 캐면서 피로도 계산
        for i in permutation:
            for _ in minerals[a:a+5]:
                fatigue += 5**(max(0,(picks_dict[_] - picks_dict[i])))
                # print(fatigue)
        
        # 기존 피로도보다 높아지면 break
            else:
                a += 5
                if fatigue >= answer:
                    break
        
        # 최소값 선택
        answer = min(answer, fatigue)
                

    return answer

# 시간초과로 못 푼 문제
# 어디를 단축시켜야할지 모르겠음