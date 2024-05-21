n = 2
num1 = 0
num2 = 1
next_number = num2
count = 1
lst = []
lst.append(num1)
lst.append(num2)
while count <= n:
    lst.append(next_number)
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print(lst)
print(lst[n])
