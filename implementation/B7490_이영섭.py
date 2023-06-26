from itertools import product

T = int(input())
for _ in range(T):
    N = int(input())
    bf = list(product([' ', '+', '-'], repeat=N-1))
    for case in bf:
        num = 2
        eval_string = '1'
        print_string = '1'
        for cs in case:
            if cs == ' ':
                eval_string += str(num)
            else:
                eval_string += cs + str(num)
            print_string += cs + str(num)
            num += 1
        result = eval(eval_string)
        # print(result, print_string)
        if result == 0:
            print(print_string)
    print()