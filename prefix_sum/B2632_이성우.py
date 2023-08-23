from collections import defaultdict

target = int(input())
n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(m)]

def suffix_sum(arr, l):
    case = defaultdict(int)
    for i in range(l):
        tmp = arr[i:] + arr[:i]
        pre = 0
        for num in tmp:
            pre += num
            case[pre] += 1
    case[sum(arr)] = 1
    return case

case_a = suffix_sum(a, n)
case_b = suffix_sum(b, m)

answer = case_a[target] + case_b[target]
for i in case_a:
    answer += case_a[i]*case_b[target-i]

print(answer)