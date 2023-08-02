def move_all_traveler():
    global exits, ans

    for i in range(1, m+1):
        if traveler[i] == exits:
            continue
        
        tx, ty = traveler[i]
        ex, ey = exits

        if tx != ex:
            nx, ny = tx, ty

            if ex > nx: 
                nx += 1
            else:
                nx -= 1

            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue

        if ty != ey:
            nx, ny = tx, ty

            if ey > ny: 
                ny += 1
            else:
                ny -= 1

            if not board[nx][ny]:
                traveler[i] = (nx, ny)
                ans += 1
                continue


def find_minimum_square():
    global exits, sx, sy, square_size
    ex, ey = exits

    for sz in range(2, n+1):
        for x1 in range(1, n-sz+2):
            for y1 in range(1, n-sz+2):
                x2, y2 = x1+sz-1, y1+sz-1

                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue

                is_traveler_in = False
                for l in range(1, m+1):
                    tx, ty = traveler[l]
                    if x1 <= tx and tx <= x2 and y1 <= ty and ty <= y2:
                        if not (tx == ex and ty == ey):
                            is_traveler_in = True

                if is_traveler_in:
                    sx = x1
                    sy = y1
                    square_size = sz

                    return


def rotate_square():
    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            if board[x][y]: 
                board[x][y] -= 1

    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            ox, oy = x-sx, y-sy
            rx, ry = oy, square_size-ox-1
            next_board[rx+sx][ry+sy] = board[x][y]

    for x in range(sx, sx+square_size):
        for y in range(sy, sy+square_size):
            board[x][y] = next_board[x][y]


def rotate_traveler_and_exit():
    global exits

    for i in range(1, m+1):
        tx, ty = traveler[i]
        if sx <= tx and tx < sx+square_size and sy <= ty and ty < sy+square_size:
            ox, oy = tx-sx, ty-sy
            rx, ry = oy, square_size-ox-1
            traveler[i] = (rx+sx, ry+sy)

    ex, ey = exits
    if sx <= ex and ex < sx+square_size and sy <= ey and ey < sy+square_size:
        ox, oy = ex-sx, ey-sy
        rx, ry = oy, square_size-ox-1
        exits = (rx+sx, ry+sy)

n, m, k = tuple(map(int, input().split()))
board = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n + 1):
    board[i] = [0] + list(map(int, input().split()))

next_board = [[0] * (n+1) for _ in range(n+1)]
traveler = [(-1, -1)] + [tuple(map(int, input().split())) for _ in range(m)]
exits = tuple(map(int, input().split()))

ans = 0
sx, sy, square_size = 0, 0, 0

for _ in range(k):
    move_all_traveler()

    is_all_escaped = True
    for i in range(1, m+1):
        if traveler[i] != exits:
            is_all_escaped = False

    if is_all_escaped: 
        break

    find_minimum_square()
    rotate_square()
    rotate_traveler_and_exit()

print(ans)
print(*exits)