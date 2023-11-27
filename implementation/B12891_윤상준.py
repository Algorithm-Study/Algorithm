s, p = map(int, input().split())
gene = {'A':0, 'C': 0, 'G': 0, 'T': 0}
code = ['A','C','G','T']
line = input()
a,c,g,t = map(int, input().split())
for i in range(p):
    gene[line[i]] += 1
answer = 0
if gene['A'] >= a and gene['C'] >= c and gene['G'] >= g and gene['T'] >= t:
    answer += 1

for i in range(len(line)-p):
    gene[line[i]] -= 1
    gene[line[i+p]] += 1
    if gene['A'] >= a and gene['C'] >= c and gene['G'] >= g and gene['T'] >= t:
        answer += 1
print(answer)