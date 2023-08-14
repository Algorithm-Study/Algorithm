t = int(input())
gears = [list(input()) for _ in range(t)]
k = int(input())
for _ in range(k):
    num,rotate = map(int, input().split())
    num -= 1
    rotates = [0]*t
    rotates[num] = rotate
    # 왼쪽 기어체크
    for i in range(num-1, -1, -1):
        # 회전하는 경우
        if gears[i][2] != gears[i+1][6]:
            rotates[i] = -rotates[i+1]
        else:
            break
    # 오른쪽 기어체크
    for i in range(num+1,t):
        if gears[i][6] != gears[i-1][2]:
            rotates[i] = -rotates[i-1]
        else:
            break
    for i in range(t):
        if rotates[i] == 1:
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        elif rotates[i] == -1:
            gears[i] = gears[i][1:] + [gears[i][0]]

print(sum(int(x[0]) for x in gears)) 