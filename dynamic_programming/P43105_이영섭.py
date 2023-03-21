def solution(triangle):
    answer = 0
    data = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    data[0][0] = triangle[0][0]
    for i in range(1, len(data)):
        data[i][0] = data[i-1][0] + triangle[i][0]
        for j in range(1, i):
            data[i][j] = max(data[i-1][j-1], data[i-1][j]) + triangle[i][j]
        data[i][-1] = data[i-1][-1] + triangle[i][-1]
    answer = max(data[-1])
    return answer