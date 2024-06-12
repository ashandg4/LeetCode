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


l = 0  # The next 0 should be placed in l.
r = len(nums) - 1  # THe next 2 should be placed in r.

i = 0
while i <= r:
    if nums[i] == 0:
        nums[i], nums[l] = nums[l], nums[i]
        i += 1
        l += 1
    elif nums[i] == 1:
        i += 1
    else:
        # We may swap a 0 to index i, but we're still not sure whether this 0
        # is placed in the correct index, so we can't move pointer i.
        nums[i], nums[r] = nums[r], nums[i]
        r -= 1
print(nums)
