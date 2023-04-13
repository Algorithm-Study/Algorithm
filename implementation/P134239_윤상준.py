def solution(k, ranges):
    squares = []
    # 각 구간별 값 구하기
    while k > 1:
        if k % 2 == 0:
            k /= 2
            squares.append(1.5*k)
        else:
            squares.append(2*k + 0.5)
            k = 3*k + 1
    start, end = 0, len(squares)
    answer = []
    for dx, dy in ranges:
        x = start + dx
        y = end + dy
        if x > y:
            answer.append(-1)
        else:
            answer.append(sum(squares[x:y]))
    return answer