# 변수 초기화
n = int(input())
arr = []
for i in range(n):
    a, b, c, d, e, f = map(int, input().split())
    arr.append([a, b, c, e, d, f])
answer = 0

# 완전 탐색
for i in range(1, 7):
    tmp = 0
    for a in arr:
        s = set([1, 2, 3, 4, 5, 6])
        s.remove(i)
        idx = a.index(i)
        i = a[5-idx]
        s.remove(i)
        tmp += max(s)
    answer = max(answer, tmp)
    
print(answer)