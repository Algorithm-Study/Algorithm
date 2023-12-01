other_side = {0:5,1:3,2:4,3:1,4:2,5:0}
n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(6):
    temp = 0
    p1,p2 = dice[0][i], dice[0][other_side[i]]
    temp += max([dice[0][x] for x in range(6) if dice[0][x] not in [p1,p2]])
    for d in range(1,n):
        index = dice[d].index(p2)
        p1, p2 = dice[d][index], dice[d][other_side[index]]
        temp += max([dice[d][x] for x in range(6) if dice[d][x] not in [p1,p2]])
    if result < temp:
        result = temp
print(result)