# Special Array With X Elements Greater Than or Equal X
nums = [0, 0]


def fun(nums):
    for i in range(0, len(nums)+1):
        count = 0
        for item in nums:
            if item >= i:
                count += 1

        if count == i:
            return i
    return -1


print(fun(nums))
