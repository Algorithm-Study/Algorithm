def solution(gems):
    answer = [0, len(gems)]
    size = len(set(gems))
    left, right = 0, 0
    gem_dict = {gems[0] : 1}
    
    while left < len(gems) and right < len(gems):
        if len(gem_dict) == size:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]       
            else:
                gem_dict[gems[left]] -= 1
                if gem_dict[gems[left]] == 0:
                    del gem_dict[gems[left]]
                left += 1
                
        else:
            right += 1
            
            if right == len(gems):
                break
                
            if gems[right] in gem_dict:
                gem_dict[gems[right]] += 1
                
            else:
                gem_dict[gems[right]] = 1
    
    return [answer[0]+1, answer[1]+1]