def solution(n):
    # maps 초기화
    maps = [[0]*i for i in range(1,n+1)]
    x, y = -1, 0 # 좌표 초기화 => 처음 시작은 아래로 내려가기 때문에 x = -1
    num = 1

    for i in range(n): # 방향
        for j in range(i, n): # 좌표 구하기
            if i % 3 == 0: # 하
                x += 1
            elif i % 3 == 1: # 우
                y += 1
            else: # 상
                x -= 1
                y -= 1
            maps[x][y] = num
            num += 1
            
    # sum(list, []) 로 2차원 list들의 요소를 합칠 수 있다
    return sum(maps, [])