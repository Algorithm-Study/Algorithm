import sys
input = sys.stdin.readline
r, c, rotation = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
directions = [[1,0],[0,1],[-1,0],[0,-1]]


for i in range(min(r,c)//2):
    x, y = i, i
    next = arr[x][y]
    for _ in range(rotation):
        for d, direction in enumerate(directions):
            if d % 2 == 0:
                for _ in range(r-1-2*i):
                    arr[x+direction[0]][y+direction[1]], next = next, arr[x+direction[0]][y+direction[1]]
                    x, y = x+direction[0], y+direction[1]

            else:
                for _ in range(c-1-2*i):
                    arr[x+direction[0]][y+direction[1]], next = next, arr[x+direction[0]][y+direction[1]]
                    x, y = x+direction[0], y+direction[1]

        arr[i+1][i] = next
        # print(next)
for row in arr:
    print(*row)
        