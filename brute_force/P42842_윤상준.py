def solution(brown, yellow):
    answer = []
    yellow_x =1
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = int(yellow / i)
            if (i+ yellow_x)*2 + 4 == brown:
                answer.append(yellow_x +2)
                answer.append(i + 2)
                print(answer)
                return sorted(answer, reverse = True)
    return answer