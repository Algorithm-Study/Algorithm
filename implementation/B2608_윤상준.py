arabic2num = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
num2arabic = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
duplictalbe = [1000,100,10,1]
n1 = input()
n2 = input()
total, i  = 0, 0
while i < len(n1):
    if i+1 < len(n1) and arabic2num[n1[i]] <  arabic2num[n1[i+1]]:
        total += arabic2num[n1[i:i+2]]
        i += 2
    else:
        total += arabic2num[n1[i]]
        i += 1
i = 0
while i < len(n2):
    if i+1 < len(n2) and arabic2num[n2[i]] <  arabic2num[n2[i+1]]:
        total += arabic2num[n2[i:i+2]]
        i += 2
    else:
        total += arabic2num[n2[i]]
        i += 1
print(total)
result = ''
for num in num2arabic:
    if total >= num:
        if num in duplictalbe:
            result += num2arabic[num] * (total//num)
            total %= num
        else:
            result += num2arabic[num]
            total -= num
print(result)