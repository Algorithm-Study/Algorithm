import sys
input = sys.stdin.readline

n = int(input())
port = list(map(int, input().rstrip().split()))
line = []

for p in port:
    if not line or line[-1] < p:
        line.append(p)
    else:
        left, right = 0, len(line)-1
        while left <= right:
            mid = (left + right) // 2
            if line[mid] < p:
                left = mid + 1
            else:
                right = mid - 1
        line[left] = p
print(len(line))