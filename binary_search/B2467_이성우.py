n = int(input())
arr = list(map(int, input().split()))

tmp_left = 0
tmp_right = n-1

ans = abs(arr[tmp_left] + arr[tmp_right])
left = tmp_left
right = tmp_right

while tmp_left < tmp_right:
    tmp = arr[tmp_left] + arr[tmp_right]
    
    if abs(tmp)  < ans:
        left = tmp_left
        right = tmp_right
        ans = abs(tmp)
        if ans == 0:
            break
        
    if tmp < 0:
        tmp_left += 1
    else:
        tmp_right -= 1
        
print(arr[left], arr[right])