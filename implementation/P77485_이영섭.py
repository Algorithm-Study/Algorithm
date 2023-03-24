def solution(rows, columns, queries):
    answer = []
    arr = [[(i-1)*columns+j for j in range(1, columns+1)] for i in range(1, rows+1)]
    print(arr)
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min = 100000
        ne = arr[x1][y2]
        # 첫번째줄
        for i in range(y2, y1, -1):
            arr[x1][i] = arr[x1][i-1]
            if arr[x1][i] < min:
                min = arr[x1][i]
        arr[x1][y1] = arr[x1+1][y1]
        if arr[x1][y1] < min:
            min = arr[x1][y1]
        # 두번째줄 ~ 마지막-1번째줄
        for i in range(x1+1, x2):
            arr[i][y1] = arr[i+1][y1]
            if arr[i][y1] < min:
                min = arr[i][y1]
            temp = arr[i][y2]
            arr[i][y2] = ne
            ne = temp
            if arr[i][y2] < min:
                min = arr[i][y2]
        for i in range(y1, y2):
            arr[x2][i] = arr[x2][i+1]
            if arr[x2][i] < min:
                min = arr[x2][i]
        arr[x2][y2] = ne
        if arr[x2][y2] < min:
            min = arr[x2][y2]
        answer.append(min)
    return answer

# 문제 접근 방법
# # 더럽지만 하나하나 다 셌다...