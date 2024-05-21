# Remove Element


# array1=[2,3,4,3,2]
# print("Original array: ",array1)

# for i in range(0,len(array1)):
#     for j in range(i+1,len(array1)):
#         if array1[i] >= array1[j]:
#             array1[i],array1[j]=array1[j],array1[i]
# print("sorted array: ",array1)

nums = [4, 3, 1, 2, 3]
val = 3

i = 0
for x in range(len(nums)):
    if (nums[x] != val):
        nums[i] = nums[x]
        i += 1
print(i)
print(nums)
