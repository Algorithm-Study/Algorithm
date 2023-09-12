def rotate(arr):
    sn = len(arr)
    sm = len(arr[0])
    tmp = [[0]*sn for _ in range(sm)]
    
    for i in range(sn):
        for j in range(sm):
            tmp[j][sn-i-1] = arr[i][j]
    return tmp


def check(i, j, arr, sticker):
    sn, sm = len(sticker), len(sticker[0])
    for x in range(sn):
        for y in range(sm):
            if arr[i+x][j+y] == 1 and sticker[x][y] == 1:
                return False
    return True
        
        
def attach(i, j, arr, sticker, answer):
    sn, sm = len(sticker), len(sticker[0])
    for x in range(sn):
        for y in range(sm):
            if sticker[x][y] == 1:
                answer += 1
                arr[i+x][j+y] = sticker[x][y]
    return arr, answer


def play(arr, sticker, answer):
    cnt = True
    r = 0
    while cnt and r <= 3:
        sn, sm = len(sticker), len(sticker[0])
        for i in range(n-sn+1):
            for j in range(m-sm+1):
                if check(i, j, arr, sticker):
                    cnt = False
                    arr, answer = attach(i, j, arr, sticker, answer)
                    return arr, answer
                    
        if cnt == True:
            sticker = rotate(sticker)
            r += 1
    return arr, answer

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
answer = 0
for _ in range(k):
    sn, sm = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(sn)]
    arr, answer = play(arr, sticker, answer)
    
print(answer)
