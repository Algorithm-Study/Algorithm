from collections import defaultdict
def solution(str1, str2):
    a = defaultdict(int)
    b = defaultdict(int)
    
    for word, s in zip([str1, str2], [a, b]):
        for i in range(len(word)-1):
            if word[i:i+2].isalpha():
                s[word[i:i+2].lower()] += 1
                
    AandB = list(a.keys()&b.keys())
    AorB = list(a.keys()|b.keys())

    for sets, funcs in zip([AandB, AorB], [min, max]):
        for e in sets[:]:
            for _ in range(funcs(a[e], b[e])-1):
                sets.append(e)
            
    if len(AorB) == 0:
        ja = 1
    else:
        ja = len(AandB)/len(AorB)
        
    return int(ja*65536)