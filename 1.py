# Two Sum
nums = [2, 7, 11, 15]
target = 9

count = 0
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if i != j and nums[i]+nums[j] == target:
            print([i, j])
