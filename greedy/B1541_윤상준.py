data = input().split('-')
total = 0
i = 0
for idx, d in enumerate(data):
    sub_total = 0
    temp = d.split('+')
    for t in temp:
        sub_total += int(t)
    if idx == 0:
        total += sub_total
    else:
        total -= sub_total
print(total)