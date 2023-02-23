def solution(lottos, win_nums):
    answer = []
    non_zero = [num for num in lottos if num != 0]
    get_num = [num for num in non_zero if num in win_nums]
    # 이미 맞춘 것 개수
    len_list = len(get_num)
    # 빈 칸 개수
    len_zero = 6 - len(non_zero)
    # 맞출 수 있는 범위
    a = 7 - len_list
    b = 7 - len_list - len_zero
    if a == 7:
        a = 6
    if b == 7:
        b = 6
    answer = [b, a]
    return answer

# 너무 쉬운 것을 가져온 것 같다...