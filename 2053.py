# Kth Distinct String in an Array

arr = ["d", "b", "c", "b", "c", "a"]
k = 2
dict1 = {}


for i in range(len(arr)):
    dict1[arr[i]] = arr.count(arr[i])
idx = 0
for item in arr:
    if dict1[item] == 1:
        idx += 1
        if idx == k:
            print(item)
print("")
