nums = input()

i = 1

while nums:
    letter = str(i)
    while letter != '' and nums != '':
        if nums[0] == letter[0]:
            nums = nums[1:]
        letter = letter[1:]
    i += 1

print(i-1)