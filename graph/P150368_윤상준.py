def solution(users, emoticons):
    answer = [0, 0]
    sale_rate = [10 ,20, 30, 40] #할인율은 10,20,30,40만 가능
    cases = []
    # 모든 할인 경우의 수 구하기
    def dfs(case, depth):
        if depth == len(case):
            cases.append(case[:])
            return
        for s in sale_rate:
            case[depth] += s
            dfs(case, depth + 1)
            case[depth] -= s # 빼주지 않으면 경우의 수가 이상하게 생성됨
    
    dfs([0] * len(emoticons), 0)
    # print(cases)
    for case in cases:
        sub = 0 
        prices = [0] * len(users)
        for idx, emoticon in enumerate(emoticons):
            for pos, user in enumerate(users):
                if user[0] <= case[idx]:
                    prices[pos] += emoticon*(1-case[idx]/100)
        for i, price in enumerate(prices):
            if price >= users[i][1]:
                sub += 1
                prices[i] = 0
        if sub >= answer[0]:
            if sub == answer[0]:
                answer[1] = max(answer[1], sum(prices))
            else:
                answer[0] = sub
                answer[1] = sum(prices)
    return answer