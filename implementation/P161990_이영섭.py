def solution(wallpaper):
    answer = []
    cnt = 0
    min_row, max_row, min_col, max_col = 51, -1, 51, -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                max_row = i if max_row < i else max_row
                max_col = j if max_col < j else max_col
                min_row = i if min_row > i else min_row
                min_col = j if min_col > j else min_col
    answer.append(min_row)
    answer.append(min_col)
    answer.append(max_row+1)
    answer.append(max_col+1)
    return answer