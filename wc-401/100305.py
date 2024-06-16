# Find the N-th Value After K Seconds

n = 5
k = 1000

lst = [1] * n
for second in range(k):
    new_lst = [1] * n
    new_lst[0] = lst[0]
    for i in range(1, n):
        new_lst[i] = (new_lst[i-1] + lst[i])
    lst = new_lst

print(lst[n-1])
