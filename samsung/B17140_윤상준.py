import sys
input = sys.stdin.readline
r, c, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(3)]

def calculate(array, mode): 
    new_matrix, length = [], 0
    for row in array:
        num_cnt, new_row = [], []
        # 갯수 새기
        for num in set(row):
            if num == 0: 
                continue
            cnt = row.count(num)
            num_cnt.append((num, cnt))
        num_cnt = sorted(num_cnt, key=lambda x:[x[1], x[0]])
        for num, cnt in num_cnt:
            new_row += [num, cnt]
        new_matrix.append(new_row)
        length = max(length, len(new_row))
    # 가장 긴 행(또는 열)의 크기에 맞춰 0 추가하기
    for row in new_matrix: 
        row += [0] * (length - len(row))
        if len(row) > 100: row = row[:100] # 크기가 100이 넘어가면 슬라이싱

    return list(zip(*new_matrix)) if mode == 'C' else new_matrix

time = 0
while True:
    if time > 100: 
        time = -1 
        break
    # (r, c)의 값이 k와 일치하면 break
    if 0 <= r-1 < len(array) and 0 <= c-1 < len(array[0]) and array[r-1][c-1] == k: 
        break 
    # 행의 개수 >= 열의 개수
    if len(array) >= len(array[0]): 
        array = calculate(array, 'R')
    else:
        array = calculate(list(zip(*array)), 'C')
    time += 1
print(time)

# list(zip(*array))를 하면 transpose 시킬 수 있음
# 전치 이외에는 문제 조건에 맞게 구현하면 됨
