line = input()
size = line.count('a')
length = len(line)
line += line
min_change = size
for i in range(length):
    min_change = min(min_change, line[i:i+size].count('b'))
print(min_change)
# 슬라이딩 윈도우를 a 크기로 설정하여 안에 있는 b의 갯수만큼 교환이 진행되어야 하는 점 이용
# 최소 교환 횟수를 찾으면 됨