nums1 = [1, 3, 2, 5]
nums2 = [4, 6]
nums3 = []

for i in nums1:
    nums3.append(i)
for j in nums2:
    nums3.append(j)
nums3.sort()
length = len(nums3)

if length % 2 == 0:
    median = (nums3[(length//2)-1]+nums3[(length//2 + 1)-1])/2
else:
    median = nums3[((length+1)//2)-1]
print(float(median))
