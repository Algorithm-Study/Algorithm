from bisect import bisect_left

lan = {"cpp": 0, "java": 1, "python": 2}
end = {"backend": 0, "frontend": 1}
exp = {"junior": 0, "senior": 1}
food = {"chicken": 0, "pizza": 1}

def get_number(temp):
    first = lan[temp[0]]
    second = end[temp[1]]
    third = exp[temp[2]]
    fourth = food[temp[3]]
    return first*8 + second*4 + third*2 + fourth

def get_number_query(temp):
    if temp[0] == "-":
        first = [0, 1, 2]
    else:
        first = [lan[temp[0]]]
    if temp[1] == "-":
        second = [0, 1]
    else:
        second = [end[temp[1]]]
    if temp[2] == "-":
        third = [0, 1]
    else:
        third = [exp[temp[2]]]
    if temp[3] == "-":
        fourth = [0, 1]
    else:
        fourth = [food[temp[3]]]
    
    ret = []
    for i in first:
        for j in second:
            for k in third:
                for l in fourth:
                    ret.append(i*8 + j*4 + k*2 + l)
    
    return ret

def solution(info, query):
    answer = []
    information = []
    idx = [0, 2, 4, 6]
    option = dict()
    option_idx = 0
    for lan in ["cpp", "java", "python"]:
        for end in ["backend", "frontend"]:
            for exp in ["junior", "senior"]:
                for food in ["chicken", "pizza"]:
                    option[option_idx] = []
                    option_idx += 1
    ifm = []
    for mation in info:
        temp = mation.split()
        ifm.append(temp)
    ifm = sorted(ifm, key = lambda x:int(x[-1]))
    for mation in ifm:
        option[get_number(mation)].append(int(mation[-1]))
    for qr in query:
        ans = 0
        temp = qr.replace("and", "").split()
        ls = get_number_query(temp)
        for i in ls:
            ans += len(option[i]) - bisect_left(option[i], int(temp[-1]))
        answer.append(ans)
                
    return answer

# 문제 접근 방법
# # O(nm)으로 접근하게 되면 50억이므로 무조건 시간초과
# # 중간에 break를 걸어 최대한 반복문을 돌지 않게 했으나 효율성에서 걸림
# # 모든 경우의 수를 만들고 해당하는 info의 점수들을 list 형태로 저장했으나 역시 효율성에서 걸림
# # info 값을 정렬하고 마지막에 탐색할 때, 이분 탐색으로 진행하여 성공
# 새로 배운 python
# # bisect 라이브러리 안의 bisect_left를 활용하면 idx값을 쉽게 구할 수 있다.
# binary search
# l = 0
# r = len(option[i])
# mid = 0
# while l < r:
#     mid = (r+l)//2
#     if option[i][mid] >= int(temp[-1]):
#         r = mid
#     else:
#         l = mid+1