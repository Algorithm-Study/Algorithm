origin = input()
result = input()
cases = [result]
while cases:
    temp = cases.pop()
    if temp == origin:
        print(1)
        exit()
    if temp.endswith('A'):
        cases.append(temp[:-1])
    if temp.endswith('B'):
        temp = temp[:-1][::-1]
        cases.append(temp)
print(0)
# 역으로 돌아가면서 체크하면 됨