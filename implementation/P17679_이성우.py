def solution(m, n, board):
    answer = 0
    twobytwo = set()
    board = [list(_) for _ in board]
    
    def search_board(a_set: set) -> set:
        # search for the same block of 2x2
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '0':
                    a_set.add((i,j))

        return a_set

    def get_point() -> int:
        # get points and mark blocks with '0'
        dx = [0,0,1,1]
        dy = [0,1,0,1]
        point = 0

        while twobytwo:
            x, y = twobytwo.pop()
            for idx in range(4):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if board[nx][ny] != '0':
                    board[nx][ny] = '0'
                    point += 1

        return point

    def rearrange_board() -> None:
        # Search from the bottom of the board
        # Replace '0' blocks with non '0' blocks
        for i in range(m)[::-1]:
            for j in range(n):
                if board[i][j] == '0':
                    for k in range(i)[::-1]:
                        if board[k][j] != '0':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
                
    while True:
        twobytwo = search_board(twobytwo)
        if twobytwo == set():
            break
        answer += get_point()
        rearrange_board()

    return answer