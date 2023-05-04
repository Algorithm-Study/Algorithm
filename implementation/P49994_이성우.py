def solution(dirs):
    # 변수 초기화
    x, y = 0, 0
    directions = {'U':[-1,0], 'D':[1,0], 'R':[0,1], 'L':[0,-1]}
    answer = set()
    
    # 이동하고 이동한 곳 기록
    for dir in dirs:
        nx = x + directions[dir][0]
        ny = y + directions[dir][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x,y,nx,ny))
            answer.add((nx,ny,x,y))
            x, y = nx, ny
            
    # 왔다갔다 하는 경우 모두 추가해줬기 때문에 반으로 나누기
    return len(answer)//2

# in 연산자는 set과 어울린다
# set은 list를 추가할수는 없고 tuple은 가능하다
