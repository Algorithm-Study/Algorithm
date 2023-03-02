# counter 사용하면 자동으로 딕셔너리 형태로 생성 : O(n)
from collections import Counter
num = int(input())
for _ in range(num):
    n = int(input())
    categories = []
    for _ in range(n):
        categories.append(input().split()[1])
    count = Counter(categories)
    cases = 1
    for c in count:
        cases *= (count[c] + 1)
    print(cases - 1)