# Number of Steps to Reduce a Number in Binary Representation to One

s = "1"
l = []
for i in s:
    l.append(int(i))

j, num = 0, 0
for item in l[::-1]:
    item *= (2**j)
    j += 1
    num += item

count = 0
while num > 1:
    if num % 2 == 0:
        num //= 2
    else:
        num += 1
    count += 1
    if num == 1:
        break
print(count)
