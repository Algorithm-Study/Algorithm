n, atk = map(int, input().split())
maxHP, culdamaged = 0, 0
for _ in range(n):
    t, a, h = map(int, input().split())
    # 몬스터
    if t == 1:
        # 나누어떨어짐: 데미지를 한번 덜 받음(선공이므로)
        if h % atk == 0:
            damaged = a*(h//atk-1)
        # 한번 더 공격해서 마무리 해야 함
        else:
            damaged = a*(h//atk)
    #물약방
    else:
        atk += a
        damaged = -h
    culdamaged += damaged
    # 누적데미지가 음수가 되는 것은 불가능
    if culdamaged < 0:
        culdamaged = 0
    maxHP = max(maxHP, culdamaged)
print(maxHP+ 1) 