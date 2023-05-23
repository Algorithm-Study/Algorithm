def solution(m, n, board):
    # 리스트 변환 통해 쉽게 제거 할 수 있도록 변환
    rboard = [[board[m-(x+1)][y] for x in range(m)] for y in range(n)]
    count = 0
    while True:
        toremove = set()
        for i in range(n-1):
            for j in range(m-1):
                if rboard[i][j] != 'X' and [rboard[i][j+1],rboard[i+1][j+1], rboard[i+1][j]].count(rboard[i][j]) == 3:
                    print(i,j, [rboard[i][j+1],rboard[i+1][j+1], rboard[i+1][j]])
                    toremove.add((i,j))
                    toremove.add((i,j+1))
                    toremove.add((i+1,j))
                    toremove.add((i+1,j+1))
        # 더 이상 제거할 수 없으면 정지
        if len(toremove) == 0:
            break
        newboard = [[] for x in range(n)]
        for i in range(n):
            added = 0
            for j in range(m):
                # 제거 대상이 아닌 경우에만 해당 행에 추가(당겨지는 효과)
                if (i,j) not in toremove:
                    newboard[i].append(rboard[i][j])
                    added += 1
            # 제거된 갯수만큼 X를 추가해서 이후 계산에도 문제없이 작동되도록 설정
            if added < m:
                newboard[i] = newboard[i] + ['X'] * (m - added)
                count += (m - added)
        # 연산 결과 적용
        rboard = newboard[:]
    return count
# 리스트 길이를 유지하면서 제거하면 되는 문제
# 변환해서 진행하면 쉽게 문제 해결 가능