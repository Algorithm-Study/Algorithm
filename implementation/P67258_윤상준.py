from collections import defaultdict
def solution(gems):
    n = len(gems)
    categories = len(set(gems))
    answer = [1,n]
    jewels = defaultdict(int)
    jewels[gems[0]] += 1
    left,right = 0,0
    while left < n and right < n:
        if len(jewels) == categories:
            if right - left < answer[1] - answer[0]:
                answer = [left+1,right+1]
            else:
                if jewels[gems[left]] == 1:
                    del jewels[gems[left]]
                else:
                    jewels[gems[left]] -= 1
                left += 1
        else:
            right += 1
            if right == n:
                break
            jewels[gems[right]] += 1
                
    return answer
# 덱보다는 투 포인터를 활용하는 것이 더 편함
# dict의 키를 제거하여 존재하는 키만 가지고 있는 것이 중요