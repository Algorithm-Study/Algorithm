from collections import defaultdict
from string import  ascii_lowercase
alphabet = defaultdict(int)
# 규칙에 의해 a,n,t,i,c는 항상 포함되는 단어
rules = ['a','n','t','i','c']
for a in ascii_lowercase:
    alphabet[a] = 0
n, k = map(int, input().split())
for rule in rules:
    alphabet[rule] = 1
words = []
# 단어 입력 받기
for _ in range(n):
    words.append(input())
answer = [0]
def dfs(start,count):
    if count == k:
        temp = 0
        for word in words:
            for w in word:
                if alphabet[w] == 0:
                    break
            else:
                temp += 1
        answer.append(temp)
        return
    
    for i in range(ord(start), ord('z')+1):
        if alphabet[chr(i)] == 0:
            alphabet[chr(i)] = 1
            dfs(chr(i), count + 1)
            alphabet[chr(i)] = 0
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    dfs('a', 5)
    print(max(answer))
# dfs를 활용한 백트래킹 문제
