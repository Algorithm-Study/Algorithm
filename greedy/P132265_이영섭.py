from collections import Counter
def solution(topping):
    answer = 0
    ubro = dict(Counter(topping))
    dbro = dict()
    for i in range(len(topping)):
        ubro[topping[i]] -= 1
        if ubro[topping[i]] == 0: del ubro[topping[i]]
        if topping[i] in dbro: dbro[topping[i]] += 1
        else: dbro[topping[i]] = 1
        if len(ubro) == len(dbro): answer += 1
    return answer

# 문제 접근 방법
# # for 문 두개를 사용해서 매번 set을 만들어 비교했는데
# # 자료구조를 여러 번 만드는 과정에서 시간초과가 발생
# # 하나씩 접근하면서 빼서 옮기는 방식으로 사용하면 시간초과 해결