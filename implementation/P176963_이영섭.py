def solution(name, yearning, photo):
    answer = []
    yearn = {name[i]: yearning[i] for i in range(len(name))}
    for ph in photo:
        temp = 0
        for person in ph:
            if person in yearn:
                temp += yearn[person]
        answer.append(temp)
    return answer