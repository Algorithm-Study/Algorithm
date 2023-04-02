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
    if temp.startswith('B'):
        temp = temp[::-1]
        cases.append(temp[:-1]) 
print(0)