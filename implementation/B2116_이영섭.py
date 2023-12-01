n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
ban = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
side = {0: [1, 2, 3, 4], 1: [0, 2, 4, 5], 2: [0, 1, 3, 5], 3: [0, 2, 4, 5], 4: [0, 1, 3, 5], 5: [1, 2, 3, 4]}
ans = 0

for i in range(6):
    bottom = dice[0][i]
    up_idx = ban[i]
    up_val = dice[0][ban[i]]
    total = max(dice[0][idx] for idx in side[i])

    for j in range(1, len(dice)):
        bottom = dice[j].index(up_val)
        up_idx = ban[bottom]
        up_val = dice[j][up_idx]
        total += max(dice[j][idx] for idx in side[bottom])

    if ans < total:
        ans = total

print(ans)
