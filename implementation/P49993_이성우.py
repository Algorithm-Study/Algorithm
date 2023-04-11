def solution(skill, skill_trees):
    answer = 0
    
    for SkillTree in skill_trees:
        i = []
        for s in SkillTree:
            if s in skill:
                i.append(skill.index(s))

        if i == list(range(len(i))):
            answer += 1

    return answer