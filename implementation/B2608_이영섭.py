a = list(input())
b = list(input())

order_lst = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
value_lst = [1, 5, 10, 50, 100, 500, 1000]

alpha_to_value = {i: j for i, j in zip(order_lst, value_lst)}
value_to_alpha = {i: j for i, j in zip(value_lst, order_lst)}


def rome_to_arabia(ls):
    past = alpha_to_value[ls[0]]
    ans = 0
    for i in ls[1:]:
        if past < alpha_to_value[i]:
            ans -= past
        else:
            ans += past
        past = alpha_to_value[i]
    ans += past
    return ans


def arabia_to_rome(val):
    for v in value_lst[::-1]:
        while val >= v:
            if str(val)[0] == "4":
                val -= 4 * v
                print(value_to_alpha[v], end="")
                print(value_to_alpha[v * 5], end="")
            elif str(val)[0] == "9":
                v //= 5
                val -= 9 * v
                print(value_to_alpha[v], end="")
                print(value_to_alpha[v * 10], end="")
            else:
                val -= v
                print(value_to_alpha[v], end="")


arabia = rome_to_arabia(a) + rome_to_arabia(b)
print(arabia)
arabia_to_rome(arabia)
