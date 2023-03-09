from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    comb = list(combinations_with_replacement(lst, n))
    max_val = 0
    for event in comb:
        lion = 0
        apeach = 0
        lion_arrow = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 10점 -> 0점
        for idx in event:
            lion_arrow[10 - idx] += 1
        for i in range(11):
            if lion_arrow[i] > info[i]:
                lion += 10 - i
            elif lion_arrow[i] == 0 and info[i] == 0:
                pass
            else:
                apeach += 10 - i
        if lion > apeach and lion - apeach > max_val:
            answer = lion_arrow
            max_val = lion - apeach
        elif lion > apeach and lion - apeach == max_val:
            for i in range(-1, -12, -1):
                if answer[i] > lion_arrow[i]:
                    break
                elif answer[i] == lion_arrow[i]:
                    continue
                else:
                    answer = lion_arrow
                    max_val = lion - apeach
    return answer

# 문제 접근 방식
# # n이 10이하 이므로 완탐
# # 어떤 방식으로 완전 탐색할 배열을 만들 것인가? - 순열, 조합, 중복순열, 중복조합
# # n개 중에서 중복하여 r개를 뽑는 것이니까 중복 조합
# # answer를 뽑는 방식
# # # 1. lion 점수와 apeach 점수를 비교하여 lion이 높아야함
# # # 2-1. lion - apeach > max_val이면 바로 바꿔주고
# # # 2-2. lion - apeach == max_val이면 뒤에서부터 보면서 숫자가 먼저 나오는 것에 따라 결정