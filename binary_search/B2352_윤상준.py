n = int(input())
sequence = list(map(int, input().split()))
sub = [sequence[0]]
pos = 0
for i in range(1, n):
    # 증가하는 부분수열 만들기
    if sub[pos] < sequence[i]:
        sub.append(sequence[i])
        pos += 1
    elif sub[pos] > sequence[i]:
        start = 0
        end = pos
        flag = 0
        # 부분수열 갱신
        while start <= end:
            mid = (start + end)//2
            if sub[mid] > sequence[i]:
                end = mid - 1
            elif sub[mid] < sequence[i]:
                start = mid + 1
            else:
                flag = 1
                break
        if flag == 0:
            sub[start] = sequence[i]
print(pos + 1)
# 가장 긴 증가하는 부분 수열을 구하기 위헤서는 하나씩 보면서 값을 갱신해야 함
