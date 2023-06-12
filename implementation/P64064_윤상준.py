import re
from itertools import permutations
def solution(user_id, banned_id):
    num = len(banned_id)
    answer = []
    banned_id = [ban.replace('*','.') for ban in banned_id]
    for cases in permutations(user_id, num):
        for i in range(num):
            if not re.match(banned_id[i], cases[i]) or len(banned_id[i]) != len(cases[i]):
                break
        else:
            cases = sorted(list(cases))
            if cases not in answer:
                answer.append(cases)
    return len(answer)
# 정규식을 활용한 와일드카드 방식을 활용하면 문자 단위의 비교가 필요없음
# 해당하는 모든 경우의 길이를 출력하면 달성