
import sys
import bisect
# 기준 상에서 이분 탐색 진행할 경우 통과
input = sys.stdin.readline
n, m = map(int, input().split())
titles = []
standard = []
for _ in range(n):
    name, limit = input().split()
    titles.append(name)
    standard.append(int(limit))
for _ in range(m):
    character = int(input())
    idx = bisect.bisect_left(standard, character)
    print(titles[idx])

# 캐릭터들 정보 상에서 이분 탐색할 경우 특정 케이스에서 실패함 
import sys
import bisect
input = sys.stdin.readline
n, m = map(int, input().split())
titles = []
for _ in range(n):
    name, limit = input().split()
    titles.append([int(limit), name])
characters = [int(input()) for _ in range(m)]
prev = 0
for title in titles:
    idx = bisect.bisect_right(characters, title[0])
    for i in range(idx - prev):
        print(title[1])
    prev = idx