def solution(name, yearning, photo):
    name_dict = {}
    answer = []
    tmp = 0
    for n, y in zip(name, yearning):
        name_dict[n] = y
    for people in photo:
        for man in people:
            if man in name_dict:
                # print(man)
                tmp += name_dict[man]
        else:
            answer.append(tmp)
            tmp = 0

    return answer