str = input()
bomb_str = input()
bomb_len = len(bomb_str)
stack_string = []

for char in str:
    stack_string.append(char)
    if char == bomb_str[-1] and ''.join(stack_string[-bomb_len:]) == bomb_str:
        for i in range(bomb_len):
            stack_string.pop()
if len(stack_string) == 0:
    print("FRULA")
else:
    print(''.join(stack_string))

# 문제 접근 방법
# # while 문과 .replace를 사용하여 접근 -> 시간초과
# # 문자열의 문자를 하나씩 읽으며 문자열을 stack처럼 활용 -> 시간초과
# # 문자열의 문자를 하나씩 읽으며 list를 활용
# 새로 배운 python
# # python의 문자열은 immutable로 글자 하나를 뒤에 붙일지라도 새 문자열을 만들고 복사하는 과정을 거침 -> 시간초과의 이유
# # '구분자'.join(list)를 활용하면 list 사이에 구분자를 넣어 문자열을 합칠 수 있다. 
# # python에는 char가 존재하지 않고 길이가 1인 문자열이 존재한다.