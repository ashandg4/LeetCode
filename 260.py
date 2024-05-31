# Single Number III
nums = [1, 2, 1, 3, 2, 5]
list1 = []
list2 = []

# Method-1

for i in nums:
    if i not in list1:
        list1.append(i)
    else:
        list2.append(i)
result = [x for x in list1 if x not in list2]
print(result)


# Method-2

# for i in nums:
#     if nums.count(i)==1:
#         list1.append(i)
# print(list1)
