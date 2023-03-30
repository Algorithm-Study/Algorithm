def solution(k, dungeons):
    # 입장 피로도가 높아 먼저 들어가야하는 던전과
    # 들어갔다 나왔을 때 피로도 소모가 적은 던전부터 탐색
    sort_dgs1 = sorted(dungeons , key=lambda x : (-(x[0]-x[1]),x[0]))
    
    # 소모 피로도가 낮고 들어갔다 나왔을 때 피로도 소모가 적은 던전부터 탐색
    sort_dgs2 = sorted(dungeons , key=lambda x : (x[1],-(x[0]-x[1])))
    print(sort_dgs1,'||',sort_dgs2)
    cnt1 = 0
    cnt2 = 0
    
    s=k
    
    # 둘 다 탐색하고 더 많이 돈 방법 선택
    for sort_dg1 in sort_dgs1:
        if k >= sort_dg1[0] and k >= sort_dg1[1]:
            k -= sort_dg1[1]
            cnt1 +=1    
    for sort_dg2 in sort_dgs2:
        if s >= sort_dg2[0] and s >= sort_dg2[1]:
            s -= sort_dg2[1]
            cnt2 +=1

    return max(cnt1,cnt2)

# 완전 탐색으로 구현
'''
from itertools import permutations as pmt
def solution(k, dungeons):
    answer = 0
    for case in pmt(dungeons):
        fatigue = k
        tmp = 0
        for dungeon in case:
            if fatigue >= dungeon[0]:
                fatigue -= dungeon[1]
                tmp += 1
        answer = max(answer, tmp)
    return answer
'''