n = int(input())
data = sorted([int(input()) for _ in range(n)])
result = set()
for d1 in data:
    for d2 in data:
        result.add(d1+d2)
answer = dict()
for d1 in data:
    for d2 in data:
        if d1 - d2 in result:
            answer[d1] = (d1,d2,d1-d2)
answer = sorted(list(answer.keys()), reverse = True)
print(answer[0])
# x,y,z,k 네개를 나누어서 푸는 문제
# x+y 에 대응하는 k-z가 존재하는지 확인하면 되는 문제