sudoku = [list(map(int, list(input()))) for _ in range(9)]
find = []

def row(x, y, val):
    for i in range(9):
        if val == sudoku[x][i] or val == sudoku[i][y]:
            return 0
    return 1
def box(x, y, val):
    sx = x//3 * 3
    sy = y//3*3
    for i in range(sx,sx + 3):
        for j in range(sy,sy+3):
            if val == sudoku[i][j]:
                return 0
    return 1
def dfs(num):
    if num == to_find:
        for i in range(9):
            print(''.join(list(map(str,sudoku[i]))))
        exit(0)
    for j in range(1,10):
        x = find[num][0] 
        y = find[num][1]
        if row(x,y,j) and box(x,y,j):
            sudoku[x][y] = j
            dfs(num+1)
            sudoku[x][y] = 0
            
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            find.append([i,j])
to_find = len(find)
dfs(0)

# 백준에 스도쿠(2580)이라고 비슷한 문제 존재 -> 같은 코드로 pass 가능(입출력만 다름)
# 풀이 후 다른 코드들을 찾은 결과 기능 별 함수 구현보다 통합된 함수로 진행하는 것이 더 빠름
# pypy3 -> 4876ms