# Patching Array

nums = [1, 3]
n = 6

count = 0
limit = 0
i = 0

while limit < n:
    if i < len(nums) and nums[i] <= limit+1:
        limit += nums[i]
        i += 1
    else:
        count += 1
        limit += limit+1
print(count)
