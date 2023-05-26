N = int(input())
ball = input()
ans = []
# red-left
red_left_move = ball.lstrip('R')
ans.append(red_left_move.count('R'))
# blue-left
blue_left_move = ball.lstrip('B')
ans.append(blue_left_move.count('B'))
# red-right
red_right_move = ball.rstrip('R')
ans.append(red_right_move.count('R'))
# blue-right
blue_right_move = ball.rstrip('B')
ans.append(blue_right_move.count('B'))

print(min(ans))