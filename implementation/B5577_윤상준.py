n = int(input())
bids = [int(input()) for _ in range(n)]
colors = [1,2,3]
result = 10001
for i in range(n):
    for color in colors:
        # 같은 색상일 경우 생략
        if color == bids[i]:
            continue
        temp = bids[:]
        temp[i] = color
        streak, before, idx = 1, temp[0], 1
        #터지는 구슬이 있는지 확인
        while idx != len(temp):
            if before == temp[idx]:
                streak += 1
            else:
                # 4개 이상인 경우 탐색 진행
                if streak >= 4:
                    temp = temp[:idx-streak] + temp[idx:]
                    idx = 0
                streak = 1
                before = temp[idx]
            
            idx += 1
        if streak >= 4:
            temp = temp[:idx-streak] + temp[idx:]
        result = min(result, len(temp))
print(result)   
