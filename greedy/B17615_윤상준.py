n = int(input())
balls = input()
min_move = min(balls.lstrip('R').count('R'), balls.rstrip('R').count('R'), balls.lstrip('B').count('B'), balls.rstrip('B').count('B'))
print(min_move)
# 네가지 조건이 존재
# 왼쪽에 R이 모이도록 R을 옮기는 경우
# 오른쪽에 R이 모이도고 R을 옮기는 경우
# 왼쪽에 B가 모이도록 B를 옮기는 경우
# 오른쪽에 B가 모이도록 B를 옮기는 경우