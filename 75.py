# # Sort Colors

nums = [2, 0, 2, 1, 1, 0]

# sorted_nums = []
# lst = [0, 1, 2]


# def f(lst, st, j):
#     for i in nums:
#         if i == lst[j]:
#             st.append(i)
#     return st


# print(f(lst, sorted_nums, 0))
# print(f(lst, sorted_nums, 1))
# print(f(lst, sorted_nums, 2))


l = 0
r = len(nums) - 1

i = 0
while i <= r:
    if nums[i] == 0:
        nums[i], nums[l] = nums[l], nums[i]
        i += 1
        l += 1
    elif nums[i] == 1:
        i += 1
    else:
        nums[i], nums[r] = nums[r], nums[i]
        r -= 1
print(nums)
