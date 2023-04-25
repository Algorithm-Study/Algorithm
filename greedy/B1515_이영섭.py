nums = input()
i = 0
while True:
    i += 1
    num = str(i)
    while len(num) > 0 and len(nums) > 0:
        if num[0] == nums[0]:
            nums = nums[1:]
        num = num[1:]
    if nums == '':
        print(i)
        break
    
# 문제 접근 방법
# # i값을 증가시키면서 input으로 들어온 값과 같은 것이 있으면
# # 하나씩 지워나가고 모두 지워졌을 때가 정답