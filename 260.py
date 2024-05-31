# Single Number III
nums = [1, 2, 1, 3, 2, 5]
list1 = []
list2 = []

# Method-1
s = set()
for i in nums:
    if i in s:
        s.remove(i)
    else:
        s.add(i)
print(list(s))


# Method-2

# for i in nums:
#     if i not in list1:
#         list1.append(i)
#     else:
#         list1.remove(i)
# print(list2)


# Method-3

# for i in nums:
#     if nums.count(i)==1:
#         list1.append(i)
# print(list1)
