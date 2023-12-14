import math
tile = [int(input()) for _ in range(6)]
answer = tile[3] + tile[4] + tile[5]
answer += math.ceil(tile[2]/4)
empty_1x1 = tile[4]*11
empty_2x2 = tile[3]*5
empty_3x3 = tile[2]%4

if empty_3x3 == 1:
    empty_2x2 += 5
    empty_1x1 += 7
elif empty_3x3 == 2:
    empty_2x2 += 3
    empty_1x1 += 6
elif empty_3x3 == 3:
    empty_2x2 += 1
    empty_1x1 += 5
    
if tile[1] > empty_2x2:
    answer += math.ceil((tile[1]-empty_2x2)/9)
    if (tile[1]-empty_2x2)%9:
        empty_1x1 += 36 - ((tile[1]-empty_2x2)%9)*4
else:
    empty_1x1 += (empty_2x2-tile[1])*4
    
if tile[0] > empty_1x1:
    answer += math.ceil((tile[0]-empty_1x1)/36)

print(answer)