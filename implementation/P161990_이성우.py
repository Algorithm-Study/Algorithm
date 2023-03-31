def solution(wallpaper):
    x = []
    y = []
    for i, row in enumerate(wallpaper):
        for j, col in enumerate(row):
            if col == '#':
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x)+1, max(y)+1]