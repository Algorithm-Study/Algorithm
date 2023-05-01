answer = 0
n = int(input())
base = list(input())

for _ in range(n-1):
    temp = base[:]
    apart = list(input())
    count = 0
    for a in apart:
        if a in temp:
            temp.remove(a)
        else:
            count += 1
    if count < 2 and len(temp) < 2:
        answer += 1
print(answer)
# 하나 추가 혹은 빼거나 교체해서 구성이 같기만 하면 비슷한 단어가 됨
# 조건만 이해하면 쉽게 풀이 가능