def solution(cards):
    length = [0]
    visited = [0] * len(cards)
    pos = cards[0] - 1
    temp = 0
    while True:
        if not visited[pos]:
            visited[pos] = 1
            temp += 1
            pos = cards[pos] - 1
        if visited[pos]:
            length.append(temp)
            temp = 0
            if visited.count(0) != 0:
                pos = visited.index(0)
            else:
                break
    length.sort()
    return length[-1] * length[-2]