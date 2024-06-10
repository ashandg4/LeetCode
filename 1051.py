# Height Checker

heights = [1, 1, 4, 2, 1, 3]
lst = heights.copy()

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(heights)
print(lst)

count = 0

for i in range(len(heights)):
    if heights[i] != lst[i]:
        count += 1
print(count)
