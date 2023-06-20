from itertools import combinations
m, h, n = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(h):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
    
for num in range(0,4):
    for case in combinations([(i, j) for i in range(n) for j in range(m-1)], num):
        tmp = [_[:] for _ in arr]
        for point in case:
            u, v = point
            if tmp[u][v] == 1:
                break
            
            if v == 0 and tmp[u][v+1] == 1:
                break
            elif tmp[u][v+1] == 1 or tmp[u][v-1] == 1:
                break
            tmp[u][v] = 1
            
        else:
            for y in range(m):
                temp = y
                for x in range(n):
                    if tmp[x][temp]:
                        temp += 1
                    elif temp > 0 and tmp[x][temp-1]:
                        temp -= 1
                if temp != y:
                    break
            else:
                print(num)
                exit()
else:
    print(-1)