import sys
from collections import defaultdict
input = sys.stdin.readline

def sol(dic):
    min_l = 10000
    max_l = 0
    for i in dic:
        for j in range(len(dic[i])-k + 1):
            length = dic[i][j+k-1] - dic[i][j] + 1
            min_l = min(min_l,length)
            max_l = max(max_l,length)
    return(min_l,max_l)
			
for _ in range(int(input())):
    word = input().rstrip()
    k = int(input())
    dic = defaultdict(list)
    
    for idx in range(len(word)):
        if word.count(word[idx]) >= k:
            dic[word[idx]].append(idx)
            
    if dic:
        print(*sol(dic))
    else:
        print(-1)