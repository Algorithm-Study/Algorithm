def solution(cards):
    box = {}
    i = 0

    for card in range(len(cards)):
        box[i] = []
        j = card
        while cards[j] != 0:
            box[i].append(cards[j])
            tmp = cards[j]
            cards[j] = 0
            j = tmp - 1

        i += 1
        
    answer = sorted(list(box.values()), key = lambda x : -len(x))
    # print(answer, cards) 
    return len(answer[0])*len(answer[1])