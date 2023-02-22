def solution(users, emoticons):
    answer = [0, 0]
    dl = []
    discount = []
    discount_percent = [10, 20, 30, 40]

    # 중복조합 만들기
    def dfs(num, discount_list, emoticons):
        if(num == emoticons):
            discount.append(list(discount_list))
            return
        for dp in discount_percent:
            discount_list.append(dp)
            dfs(num+1, discount_list, emoticons)
            discount_list.pop()
            
    dfs(0, dl, len(emoticons))
    
    # 완전 탐색으로 조건에 맞게 답 구하기
    for dis in discount:
        add_service = 0
        sales = 0
        for user in users:
            emo_price = [(100-x)*y//100 for x, y in zip(dis, emoticons) if x >= user[0]]
            if sum(emo_price) >= user[1]:
                add_service += 1
            else:
                sales += sum(emo_price)
        if add_service > answer[0]:
            answer[0] = add_service
            answer[1] = sales
        elif add_service == answer[0] and sales > answer[1]:
            answer[1] = sales
    return answer

# 문제 접근 방법
# #처음에는 backtracking 쪽으로 생각하였으나 user가 여러명인데 동시에 backtracking을 진행하는 것은 경우의 수가 너무 많다고 판단하여 완탐으로 변경

# 새로 배운 python 
# #10 list(discount_list) list를 안해주면 얕은 복사로 인하여 값이 계속 변경
# #24 zip을 활용하여 element-wise 연산을 쉽게 구현할 수 있음