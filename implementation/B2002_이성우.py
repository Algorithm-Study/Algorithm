n = int(input())
in_ = {}
out = []
answer = 0

for i in range(n):
    car = input()
    in_[car] = i
    
for i in range(n):
    car = input()
    out.append(car)

for i in range(n-1):
    for j in range(i+1, n):
        if in_[out[i]] > in_[out[j]]:
            answer += 1
            break

print(answer)