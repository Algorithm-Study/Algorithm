import sys
n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
start, end = 0, n-1
abs_min = sys.maxsize
answer = [0, 0]
while start < end:
    if liquids[start] + liquids[end] == 0:
        print(liquids[start], liquids[end])
        exit(0)
    if liquids[start] + liquids[end] < 0:
        if abs(liquids[start] + liquids[end]) < abs_min:
            answer = [liquids[start], liquids[end]]
            abs_min = abs(liquids[start] + liquids[end])
        start += 1
    else:
        if abs(liquids[start] + liquids[end]) < abs_min:
            answer = [liquids[start], liquids[end]]
            abs_min = abs(liquids[start] + liquids[end])
        end -= 1
print(answer[0], answer[1])
# 정렬 후 양쪽 끝에서 조건에 따라서 인덱스를 줄여나가면 되는 문제