def isbalanced(s):
	cnt = 0
	for c in s:
		if c == '(': cnt += 1
		elif c == ')': cnt -= 1

	if cnt == 0: return True
	else: return False

def iscorrect(s):
	stack = []
	stack.append(s[0])
	for i in range(1, len(s)):
		if len(stack) == 0 or stack[-1] == ')' or (stack[-1] == '(' and s[i] == '('):
			stack.append(s[i])
		else:
			stack.pop()
	if len(stack)==0: return True
	else: return False

def solution(p):
	answer = ''
	u, v = '', ''
	if len(p)==0 or iscorrect(p): return p

	for i in range(2, len(p) + 1, 2):
		if isbalanced(p[0:i]):
			u=p[0:i]
			v=p[i:len(p)]
			break

	if iscorrect(u):
		answer += u + solution(v)
	else:
		answer += '(' + solution(v) + ')'
		for c in u[1:-1]:
			if c=='(': answer += ')'
			else: answer += '('

	return answer