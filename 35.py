
def searchPos(nums, target):
    l = 0
    r = len(nums)

    while l < r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m

    return l


print(searchPos([1, 3, 5, 6], 5))
