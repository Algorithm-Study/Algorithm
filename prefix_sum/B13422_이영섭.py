T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    money = list(map(int, input().split()))
    if N == M:
        if sum(money) < K:
            print(1)
        else:
            print(0)
    else:
        for i in range(M-1):
            money.append(money[i])
        max_m, ans = 0, 0
        sum_m = sum([money[i] for i in range(M)])
        if sum_m < K:
            ans += 1
        for i in range(N-1):
            sum_m -= money[i]
            sum_m += money[i+M]
            if sum_m < K:
                ans += 1
        print(ans)
