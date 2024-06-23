# Minimum Average of Smallest and Largest Elements

nums = [1, 2, 3, 7, 8, 9]
n = len(nums)
averages = []

for i in range(1, (n//2)+1):
    mx = max(nums)
    mn = min(nums)
    nums.remove(mx)
    nums.remove(mn)
    avg = (mx+mn)/2
    averages.append(avg)

print(min(averages))
