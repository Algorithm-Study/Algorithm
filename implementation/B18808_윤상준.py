n,m,k = map(int, input().split())
notebook = [[0]*m for _ in range(n)]
for _ in range(k):
    sn,sm = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(sn)]
    # 놓을 수 있는 지 체크
    rotate = 0
    attach = 0
    while rotate <= 3:
        # 붙인 경우 중단
        if attach:
            break
        for i in range(n-sn+1):
            for j in range(m-sm+1):
                is_possible = 1
                for a in range(sn):
                    for b in range(sm):
                        # 놓을 수 없는 경우
                        if sticker[a][b] == 1 and notebook[i+a][j+b] == 1:
                            is_possible = 0
                            break
                    # 반복문 부수기 위해 설정
                    if not is_possible:
                        break
                # 붙이는 것이 가능한 경우 붙이기 진행
                if is_possible:
                    attach = 1
                    for a in range(sn):
                        for b in range(sm):
                            if sticker[a][b] == 1:
                                notebook[i+a][j+b] = sticker[a][b]
                    break
            # 반복문 부수기 위한 용도
            if attach:
                break
        # 부착할 공간이 없으므로 회전
        if not attach:
            rotate += 1
            rsticker = [[0]*sn for _ in range(sm)]
            # 회전
            for a in range(sn):
                    for b in range(sm):
                        rsticker[b][sn-1-a] = sticker[a][b]
            sticker = [x[:] for x in rsticker]
            sn,sm = sm, sn
total = 0
for note in notebook:
    total += sum(note)
print(total)
# 회전에 주의하면 쉽게 풀 수 있는 문제