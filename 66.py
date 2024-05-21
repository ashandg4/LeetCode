# Plus One

a = [1, 2, 3]

sum = 0
x = len(a)-1

for i in a:
    z = i*(10**x)
    sum += z
    x -= 1


new_sum = sum+1
print(sum)

l1 = []
a = 0
b = new_sum
while new_sum > 0:
    a = new_sum % 10
    new_sum //= 10

    l1.append(a)

l2 = l1[::-1]

print(l2)
