# Sum of Square Numbers

import math
c = 4


# Method-1

# def check(num):
#     for i in range(num):
#         for j in range(i):
#             if (i**2)+(j**2) == num:
#                 return True

#     return False
# print(check(c))


# Method-2

def sol():
    a = 0
    b = int(math.sqrt(c))
    while a <= b:
        sum = a**2+b**2
        if sum == c:
            return True
        if sum < c:
            a += 1
        else:
            b -= 1
    return False


print(sol())
