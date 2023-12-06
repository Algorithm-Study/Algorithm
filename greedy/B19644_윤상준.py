l = int(input())
shoot, damage = map(int, input().split())
mine = int(input())
zombies = [0] + [int(input()) for _ in range(l)]
damages = [0]*(l+1)
for i in range(1,l+1):
    current = damages[i-1] - damages[max(0,i-shoot)]
    # 기관총 사살이 가능한 경우
    if zombies[i] <= current + damage:
        damages[i] = damages[i-1] + damage
        continue
    # 기관총 사살이 불가능한 경우
    else:
        if mine:
            mine -= 1
            damages[i] = damages[i-1]
        else:
            print('NO')
            exit()
print('YES')