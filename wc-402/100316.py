# Maximum Total Damage With Spell Casting

power = [1, 1, 3, 4]

n = len(power)
subsets = [[]]

for i in power:
    new_subsets = []
    for j in subsets:
        x = j+[i]
        new_subsets.append(x)
    subsets.extend(new_subsets)
print(subsets)

diff_set = [[]]
for i in subsets:
    n = len(i)
    difference = []
    for k in range(n):
        for l in range(k+1, n):
            diff = abs(i[k]-i[l])
            if diff != 1 or diff != 2:
                difference.append(diff)
    print(difference)
