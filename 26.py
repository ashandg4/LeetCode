# Remove Duplicates from Sorted Array

nums = [1, 1, 2]
i = 0
for num in nums:
    if i < 1 or num > nums[i - 1]:
        nums[i] = num
        i += 1
print(i)
