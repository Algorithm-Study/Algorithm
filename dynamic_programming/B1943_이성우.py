import sys
input = sys.stdin.readline

answer = []
while True:
    try:
        n = int(input().rstrip())
        arr = [0]*(50_001)
        total = 0
        coins = []
        arr[0] = 1
        for _ in range(n):
            coin, m = map(int, input().split())
            total += coin*m
            coins.append([coin, m])
            
        if total % 2 == 0:
            for coin, m in coins:
                for i in range(50_000, -1, -1):
                    if arr[i] == 1:
                        for j in range(1, m + 1):
                            if i + coin * j <= 50_000:
                                arr[i + coin*j] = 1   

            if arr[total // 2] == 1:
                answer.append(1)
            else:
                answer.append(0)
                
        else:
            answer.append(0)
    except:
        print(*answer, sep='\n')
        break
