from collections import defaultdict

N = int(input())
ent, exi = [], []
for _ in range(N):
    ent.append(input())
for _ in range(N):
    exi.append(input())
i_num, o_num, ans = 0, 0, 0
car_number = defaultdict(int)

while o_num < N:
    if ent[i_num] == exi[o_num]:
        i_num += 1
        o_num += 1
    elif car_number[ent[i_num]] == 1:
        i_num += 1
    else:
        car_number[exi[o_num]] = 1
        o_num += 1
        ans += 1
print(ans)
