import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
l.sort()
    
i = 0
j = n-1
a = i
b = j
answer = l[a] + l[b]
while i < j:
    num_sum = l[i] + l[j]
    if abs(answer) > abs(num_sum):
        answer = abs(num_sum)
        a = i
        b = j

    if num_sum < 0:
        i += 1
    elif num_sum > 0:
        j -= 1
    else:
        a = i
        b = j
        # break 안넣으면 시간 초과
        break

print(l[a], l[b])