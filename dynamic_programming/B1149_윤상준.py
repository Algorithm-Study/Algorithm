#앞에만 신경쓰면 됨
import copy
n = int(input())
origin_data = []
for _ in range(n):
    origin_data.append(list(map(int, input().split())))
max_total = 1000 * len(origin_data)+ 1
for i in range(3):
    total = 0
    data = copy.deepcopy(origin_data)
    for idx, d in enumerate(data):
        if idx == 0:
            total += data[idx][i]
            data[idx+1][i] = 1001
        else:
            total += min(d)
            pos = d.index(min(d))
            if idx != len(data) -1:
                data[idx+1][pos] = 1001
    if total < max_total:
        print(total)
        max_total = total
print(max_total)

#=====================================
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1,len(data)):
    data[i][0] += min(data[i-1][1], data[i-1][2])
    data[i][1] += min(data[i-1][0], data[i-1][2]) 
    data[i][2] += min(data[i-1][1], data[i-1][0])

print(min(data[len(data)-1]))  
