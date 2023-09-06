import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
animal = [0, 0]

for i in range(2, n+1):
    a, b, c = input().split()
    b, c = int(b), int(c)
    arr[c].append(i)
    if a == 'S':
        animal.append(b)
    else:
        animal.append(-b)

def dfs(num):
    answer = 0
    
    for i in arr[num]:
        answer += dfs(i)
        
    if animal[num] < 0:
        answer = max(answer+animal[num], 0)
    else:
        answer += animal[num]
        
    return answer
    
print(dfs(1))
