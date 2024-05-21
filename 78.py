nums = [1, 2, 3]
n = len(nums)
subsets = [[]]

for i in nums:
    new_subsets = []
    for j in subsets:
        # Add the current item (i) to each existing subset
        x = j+[i]
        # Add the new subset to the list of subsets (new_subsets)
        new_subsets.append(x)
    # Add the newly generated subsets (new_subsets) to the main list of subsets (subsets)
    subsets.extend(new_subsets)

print(subsets)
