n = int(input())
in_order, out_order  = {}, []
for i in range(n):
    in_order[input()] = i
for _ in range(n):
    out_order.append(input())
count = 0
for i in range(n-1):
    for j in range(i+1,n):
        if in_order[out_order[i]] > in_order[out_order[j]]:
            count += 1
            break
print(count)