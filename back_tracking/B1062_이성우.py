from itertools import combinations
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

def choose_alpha(n, start):
    global answer
    if n == 0:
        answer = max(answer, check())
        return
    for i in range(start, len(alpha_list)):
        alpha.append(alpha_list[i])
        choose_alpha(n-1, i+1)
        alpha.pop()


def check():
    answer = 0
    for word in words:
        isRead = True
        for i in range(4, len(word)-4):
            if word[i] not in alpha:
                isRead = False
                break
        if isRead:
            answer += 1
    return answer

answer = 0
if k < 5:
    print(0)
    exit()
else:
    choose_alpha(k-5, 0)
    print(answer)