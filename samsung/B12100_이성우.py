from itertools import combinations_with_replacement as cwr
from itertools import product
from itertools import permutations as pmt
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
directions = {'up':(1, 0), 'left':(0, -1), 'right':(0, 1), 'down':(-1,0)}
answer = 0

def direction(directions):
    dx, dy = directions
        
    while True:
        tmp = [_ for _ in arr]
        if directions == (1,0) or directions == (0, -1):
            for y in range(n):
                for x in range(n-1):
                    if directions == (0, 1) or directions == (0, -1):
                        x, y = y, x

                    if arr[x][y] == arr[x+dx][y+dy]:
                        arr[x][y] += arr[x+dx][y+dy]
                        arr[x+dx][y+dy] = 0
                    elif arr[x][y] == 0:
                        arr[x][y] = arr[x+dx][y+dy]
                        arr[x+dx][y+dy] = 0

        elif directions == (-1, 0):
            for y in range(n-1,-1,-1):
                for x in range(n-1,0,-1):

                    if arr[x][y] == arr[x+dx][y]:
                        arr[x][y] += arr[x+dx][y]
                        arr[x+dx][y] = 0
                    elif arr[x][y] == 0:
                        arr[x][y] = arr[x+dx][y]
                        arr[x+dx][y] = 0
                         
        elif directions == (0, 1):
            for y in range(n-1,0,-1):
                for x in range(n-1,-1,-1):

                    if arr[x][y] == arr[x-dx][y-dy]:
                        arr[x][y] += arr[x-dx][y-dy]
                        arr[x-dx][y-dy] = 0
                    elif arr[x][y] == 0:
                        arr[x][y] = arr[x-dx][y-dy]
                        arr[x-dx][y-dy] = 0  

        if arr == tmp:
            break
        
for cases in product(['up', 'left', 'right', 'down'],repeat=1):
    temp = [_ for _ in arr]
    # print(cases)
    for case in cases:
        direction(directions[case])
    tmp = max(map(max,arr))
    print(arr, cases)
    answer = max(answer, tmp)
print(answer)