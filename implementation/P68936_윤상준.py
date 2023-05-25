def compress(x,y, length, arr, answer):
    zero, one = 0,0
    for i in range(x, x+length):
        for j in range(y, y+length):
            if arr[i][j] == 0:
                zero += 1
            else:
                one += 1
    if zero !=0 and one != 0:
        half = length//2
        compress(x,y,half, arr,  answer)
        compress(x+half, y, half, arr,  answer)
        compress(x, y+half, half, arr,  answer)
        compress(x+half, y+half, half, arr,  answer)
    elif zero == 0:
        answer[1] -= length**2 - 1
    else:
        answer[0] -= length**2 - 1
def solution(arr):
    n = len(arr)
    answer = [0,0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                answer[0] += 1
            else:
                answer[1] += 1
    half = n//2
    compress(0,0,n, arr, answer)
    return answer
# 재귀로 풀면 되는 문제
# 시작 전에 0과 1의 갯수 카운트 후 계산하면서 압축이 되는 경우 값을 줄이면 됨