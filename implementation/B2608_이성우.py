str1 = input()
str2 = input()

def convert_to_num(string):
    convert = {'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
                }
    num = 0
    for idx in range(len(string)-1):
        if convert[string[idx]] >= convert[string[idx+1]]:
            num += convert[string[idx]]
        else:
            num -= convert[string[idx]]
    num += convert[string[-1]]
    return num


def convert_to_roman(num):
    convert_1000 = ['','M','MM','MMM']
    convert_100 = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    convert_10 = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    convert_1 = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    num = list(str(num))
    num_1, num_10, num_100, num_1000 = 0, 0, 0, 0
    if num:
        num_1 = int(num.pop())
    if num:
        num_10 = int(num.pop())
    if num:
        num_100 = int(num.pop())
    if num:
        num_1000 = int(num.pop())
    string = convert_1000[num_1000] + convert_100[num_100] + convert_10[num_10] + convert_1[num_1]
    return string


num = convert_to_num(str1) + convert_to_num(str2)
print(num)
print(convert_to_roman(num))
