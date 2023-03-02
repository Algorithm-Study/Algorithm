#메모리:131660KB / 시간 4784ms
n, m = map(int,input().split())
var = list(map(int, input().split()))
data = [0]
for idx,v in enumerate(var):
    data.append(data[idx] + v)
for _ in range(m):
    i, j = map(int, input().split())
    if i - 1 > 0:
        print(data[j] - data[i - 1])
    else:
        print(data[j])