from collections import deque
gears = [list(input()) for _ in range(4)]
n = int(input())
for _ in range(n):
    gnum, dir = map(int, input().split())
    gnum -= 1
    # 왼쪽 확인
    check = gears[gnum][6]
    gdir = dir
    for i in range(gnum-1, -1, -1):
       if check != gears[i][2]:
           check = gears[i][6]
           temp = deque(gears[i])
           gdir *= -1
           temp.rotate(gdir)
           gears[i] = list(temp)
       else:
           break
    # 오른쪽 확인
    check = gears[gnum][2]
    gdir = dir
    for i in range(gnum+1,4):
       if check != gears[i][6]:
           check = gears[i][2]
           temp = deque(gears[i])
           gdir *= -1
           temp.rotate(gdir)
           gears[i] = list(temp)
       else:
           break
    # 선택한 톱니바퀴 회전
    temp = deque(gears[gnum])
    temp.rotate(dir)
    gears[gnum] = list(temp)
total = sum([2**x if gears[x][0] == '1' else 0 for x in range(4)])
print(total)
# 조건에 맞게 회전만 시키면 되는 문제
# 이후 12시 값이 1인 경우에만 점수를 얻도록 하면 됨
            