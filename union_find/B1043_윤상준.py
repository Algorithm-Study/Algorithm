n, m = map(int, input().split())
gt = set(list(map(int, input().split()))[1:])
parties = [set(list(map(int, input().split()))[1:]) for _ in range(m)]
count, i = 0, 0
while i < m:
    if parties[i] & gt:
        if parties[i]- gt:
            gt = gt.union(parties[i])
            i, count = 0, 0 
            continue
    else:
        count += 1
    i += 1
print(count)

# 진실을 알게 된 사람을 계속 갱신하면 되는 문제
# n과 m도 작아서 시간복잡도 고려 필요 X