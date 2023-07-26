import sys
input = sys.stdin.readline
change = 10_000_000

while True:
    try:
        hole = int(input())*change
        n = int(input())
        pieces = sorted([int(input()) for _ in range(n)])
        p1, p2 = 0, n-1
        while p1 < p2:
            if pieces[p1] + pieces[p2] == hole:
                print(f'yes {pieces[p1]} {pieces[p2]}')
                break
            elif pieces[p1] + pieces[p2] > hole:
                p2 -= 1
            else:
                p1 += 1
        else:
            print('danger')
    except:
        break

# 최대 케이스 수가 들어오지 않으므로 try except 사용
# 구멍은 cm이고 조각은 나노미터이므로 주의