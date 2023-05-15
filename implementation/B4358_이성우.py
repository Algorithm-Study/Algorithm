import sys
from collections import defaultdict
trees = sys.stdin.readlines()
trees_dict = defaultdict(int)
for tree in trees:
    trees_dict[tree.rstrip()] += 1
    
answer = sorted(trees_dict.keys())
for _ in answer:
    print(_,f'{round(trees_dict[_]/sum(trees_dict.values())*100, 4):.4f}')