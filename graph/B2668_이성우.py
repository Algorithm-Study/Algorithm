n = int(input())
arr = [int(input()) for _ in range(n)]
# print(arr)
answer = set()
check = set()

for i in range(1, n+1):
    if i in check:
        continue
    check.add(i)
    
    tmp1 = set()
    tmp2 = set()
    # immutable 객체는 x = y = 0처럼 한줄로 써도 다른 메모리 주소를 가르키지만
    # mutable 객체는 같은 메모리 주소를 가르키게 된다
    tmp1.add(i)
    
    x = i
    while arr[x-1] not in tmp2:
        tmp2.add(arr[x-1])
        x = arr[x-1]
        tmp1.add(x)
    if tmp1 == tmp2:
        answer.update(tmp1)
        
answer = sorted(answer)

print(len(answer))
print(*answer, sep='\n')