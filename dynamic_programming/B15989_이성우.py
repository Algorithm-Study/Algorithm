arr = [1]*10001

for idx in range(2, 10001):
    arr[idx] += arr[idx-2]
for idx in range(3, 10001):
    arr[idx] += arr[idx-3]
    
for _ in range(int(input())):
    n = int(input())
    print(arr[n])