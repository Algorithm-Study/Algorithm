def solution(wallpaper):
    row_list = []
    column_list = []
    for idx, wall in enumerate(wallpaper):
        if '#' in wall:
            row_list.append(idx)
        for pos, w in enumerate(wall):
            if w == '#':
                column_list.append(pos)
    answer = [min(row_list), min(column_list), max(row_list)+1, max(column_list)+1]
    return answer