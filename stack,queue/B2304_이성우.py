n = int(input())
garage = []
right = []
num_max = 0
answer = 0
for _ in range(n):
    x, h = map(int, input().split())
    num_max = max(num_max, h)
    garage.append([x, h])
    
garage.sort(key= lambda x : x[0])

while True:
    x, h = garage.pop()
    if h == num_max:
        answer = h
        h_max = [x, h]
        break
    else:
        right.append([x, h])

r_max = 0
r_answer = []
for r in right:
    if r_max <= r[1]:
        r_answer.append(r)
        r_max = r[1]
r_answer += [h_max]

l_max = 0
l_answer = []
for l in garage:
    if l_max <= l[1]:
        l_answer.append(l)
        l_max = l[1]
l_answer += [h_max]


for i in range(len(r_answer)-1):
    answer += (r_answer[i][0] - r_answer[i+1][0])*r_answer[i][1]

for i in range(len(l_answer)-1):
    answer += (l_answer[i+1][0]- l_answer[i][0])*l_answer[i][1]
    
print(answer)