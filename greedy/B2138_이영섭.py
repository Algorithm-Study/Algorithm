N = int(input())
data = list(map(int, input()))
mokpyo = list(map(int, input()))


def change(data, mokpyo):
    new_data = data[:]
    cnt = 0
    for i in range(1, N):
        if new_data[i-1] == mokpyo[i-1]:
            continue
        cnt += 1
        for idx in range(i-1, i+2):
            if idx < N:
                new_data[idx] = 1 - new_data[idx]
    if new_data == mokpyo:
        return cnt
    else:
        return 1e9


ans = change(data, mokpyo)
data[0], data[1] = 1 - data[0], 1 - data[1]
ans = min(ans, change(data, mokpyo) + 1)
if ans != 1e9:
    print(ans)
else:
    print(-1)
