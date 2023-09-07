n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))
is_possible = [0]
for weight in weights:
    temp = []
    for i in is_possible:
        temp.append(i+weight)
        temp.append(abs(i-weight))
    is_possible = list(set(is_possible) | set(temp))
result = []
for marble in marbles:
    if marble in is_possible:
        result.append('Y')
    else:
        result.append('N')
print(*result)
# 다차원 dp table을 구성하지 않아도 문제 해결 가능