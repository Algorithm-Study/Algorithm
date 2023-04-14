def solution(phone_book):
    answer = True
    pd = dict()
    for pn in phone_book:
        pd[pn] = 1
    for pn in phone_book:
        pd.pop(pn)
        temp = ''
        for i in range(len(pn)):
            temp += pn[i]
            if temp in pd:
                return False
        pd[pn] = 1
    return answer

# 문제 접근 방법
# # n이 100만이므로 바로 떠오르는 n^2의 알고리즘을 쓰면 시간초과
# # 모든 값을 dict에 넣고 하나씩 빼면서 비교
# # 비교 대상이 된 전화번호를 한글자씩 추가하면서 전화번호부에 있는지 확인
# # 20*100만 이므로 2000만번안으로 해결 가능