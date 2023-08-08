n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort()

arr_sum = set()
for i in arr:
    for j in arr:
        arr_sum.add(i+j)

answer = 0
for i in range(n)[::-1]:
    for j in range(i+1):
        if arr[i]-arr[j] in arr_sum:
            print(arr[i])
            exit()