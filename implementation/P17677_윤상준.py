from collections import Counter
def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    answer = 0
    set1, set2 = [], []
    for i in range(len(str1)-1):
        pos1,pos2 = str1[i:i+2]
        if ord('A')<= ord(pos1) <= ord('Z') and ord('A')<= ord(pos2) <= ord('Z'):
            set1.append(pos1+pos2)
    for i in range(len(str2)-1):
        pos1,pos2 = str2[i:i+2]
        if ord('A')<= ord(pos1) <= ord('Z') and ord('A')<= ord(pos2) <= ord('Z'):
            set2.append(pos1+pos2)
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    intersection = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    if len(union) == 0:
        jaccard = 65536
    else:
        jaccard = int(len(intersection) / len(union) * 65536)
    return jaccard
# 다중집합을 생성해야 함(그냥 집합으로는 불가능)
# Counter를 활용할 때 집합처럼 합집합과 교집합을 계산할 수 있음
# 카운터의 요소들만 가져와서 자카드 유사도를 구하면 됨