# Minimum Increment to Make Array Unique

nums = [1, 2, 2]

nums.sort()
count = 0
for i in range(1, len(nums)):
    if nums[i] <= nums[i - 1]:
        diff = nums[i - 1] - nums[i] + 1
        nums[i] += diff
        count += diff
print(count)
