N, K, P, X = map(int, input().split())
banjeon = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
           [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
           [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
           [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
           [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

X = str(X).zfill(K)
ans = 0
for i in range(1, N+1):
    cnt, str_i = 0, str(i).zfill(K)
    for x, s in zip(X, str_i):
        cnt += banjeon[int(x)][int(s)]
        if cnt > P:
            break
    else:
        ans += 1
print(ans-1)