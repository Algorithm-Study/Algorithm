from collections import Counter
import sys
input = sys.stdin.readline
woods = []
while True:
    wood = input().rstrip()
    if not wood:
        break
    woods.append(wood)
length = len(woods)
woods.sort()
classifier = Counter(woods)
for cl in classifier:
    print(f'{cl} {classifier[cl]/length*100 :.4f}')

# 카운터 활용해서 각 나무 빈도 계산 
# fstring에서의 소수점 표기 방법에 대해서 알게 됨