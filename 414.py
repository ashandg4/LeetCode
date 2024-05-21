# Third Maximum Number

nums = [2, 2, 3, 1]
nums2 = []
[nums2.append(value) for value in nums if value not in nums2]


if len(nums2) >= 3:
    count = 0
    while count < 2:
        maximum = nums2[0]
        for num in nums2:
            if num > maximum:
                maximum = num
        nums2.remove(maximum)
        count += 1

print(max(nums2))
