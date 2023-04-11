def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for tree in skill_trees:
        tree = list(tree)
        index_list = []
        flag = 0 
        for idx, sk in enumerate(skill):
            if sk in tree and len(index_list) == idx:
                index_list.append(tree.index(sk))
            elif sk in tree and len(index_list) != idx:
                flag = 1
                break
        if index_list == sorted(index_list) and flag == 0:
            print(tree)
            print(index_list)
            answer += 1
    return answer