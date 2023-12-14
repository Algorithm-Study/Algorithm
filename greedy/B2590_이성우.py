import math
tile = [int(input()) for _ in range(6)]
answer = tile[3] + tile[4] + tile[5]
answer += math.ceil(tile[2]/4)
three = tile[2]%4
two = tile[3]*5
one = tile[4]*11
if three == 1:
    two += 5
    one += 7
elif three == 2:
    two += 3
    one += 6
elif three == 3:
    two += 1
    one += 5
if tile[1] > two:
    answer += math.ceil((tile[1]-two)/9)
    one += (36 - ((tile[1]-two)%9)*4)
else:
    one += (two-tile[1])*4
    
if tile[0] > one:
    answer += math.ceil((tile[0]-one)/36)

print(answer)