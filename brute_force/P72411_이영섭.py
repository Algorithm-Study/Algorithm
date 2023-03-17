from itertools import combinations

def solution(orders, course):
    answer = []
    menu_dict = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
    for od in orders:
        menu = list(od)
        menu.sort()
        for cou in course:
            if len(menu) < cou:
                break
            bf = list(combinations(menu, cou))
            for temp in bf:
                if temp in menu_dict[cou-2]:
                    menu_dict[cou-2][temp] += 1
                else:
                    menu_dict[cou-2][temp] = 1
            
    for cou in course:
        tl = list(sorted(menu_dict[cou-2].items(), reverse=True, key=lambda md:md[1]))
        if tl:
            for temp in tl:
                # print(temp)
                if temp[1] == tl[0][1] and tl[0][1] >= 2:
                    answer.append(''.join(temp[0]))
                else:
                    break
    answer.sort()
    return answer

# 문제 접근 방법
# # 26C2 ~ 26C10의 모든 경우를 구하려 했으나 불가능할 것 같아서
# # 각 order 별로 course의 개수만큼만 경우를 셈
# # course의 범위가 2~10 이므로 dict를 8개 만들어서 list 내부에서 관리