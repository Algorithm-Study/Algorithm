import sys
from bisect import bisect_left
input = sys.stdin.readline
n, tc = map(int, input().split())
names = []
numbers = []
for _ in range(n):
    name, number = input().split()
    names.append(name)
    numbers.append(int(number))
    
def bi(case):
    left = 0
    right = len(names) - 1
    while left <= right:
        middle = (left + right) // 2
        if case > numbers[middle]:
            left = middle + 1
        else:
            right = middle - 1
    print(names[left])
    
for _ in range(tc):
    case = int(input())
    bi(case)
    
# bisect 함수를 호출해서 해결하면 좀더 빠르다
# for _ in range(tc):
#     print(names[bisect_left(numbers,int(input()))])