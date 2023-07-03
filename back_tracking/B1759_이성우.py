from itertools import combinations

L, C = map(int, input().split())
arr = input().split()
arr.sort()

for cases in combinations(arr, L):
    
    tmp = 0
    for c in cases:
        if c in set(['a', 'e', 'i', 'o', 'u']):
            tmp += 1
    
    if tmp == 0 or L - tmp <= 1:
        continue  
    
    print(''.join(sorted(cases)))
    