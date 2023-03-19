def digit_to_bin(num):
    ans = ""
    while num > 0:
        ans += str(num % 2)
        num //= 2
    ans = ans[::-1]
    tree_len = 2
    while tree_len - 1 < len(ans):
        tree_len *= 2
    ans = (tree_len - 1 - len(ans)) * '0' + ans
    return ans

def is_it_bin_tree(num):
    if len(num) == 1:
        return 1
    center = len(num) // 2
    if num[center] == '0' and not all(n == '0' for n in num):
        return 0
    return is_it_bin_tree(num[:center]) and is_it_bin_tree(num[center+1:])
        
def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(is_it_bin_tree(digit_to_bin(num)))
    return answer

# 문제 접근 방법
# # 짝수일 때 앞뒤로 0을 넣어주는 두가지를 이진 트리인지 판단하여 재귀로 return하려 했으나
# # 그렇게 되면 기존 number와 값이 달라지기 때문에 잘못된 접근
# # 기존 값은 유지하되 완전 이진 트리의 형태를 갖추려면 앞에 0을 채워 넣어야함
# # 이때 부모가 0인데 자식 중에 1이 있으면 이진트리가 아니므로 0을 return하고
# # 나머지의 경우에는 left와 right값을 재귀로 구하여 결과를 return
# 새로 배운 python
# # all(조건 for iterable 객체): 조건이 모두 참이면 True 하나라도 틀리면 False를 return
# # := 할당하고 return함
# # ex) if result := 'walrus' in (s := 'walrus eat kimchi'): 
# # ## s에 문자열을 할당하고, 'walrus' in s를 result에 할당하고, result가 참인지 판단