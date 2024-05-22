# Reverse Integer
x = -2147483648


def rev(x):
    l1 = []
    b = x
    while x > 0:
        rem = x % 10
        x //= 10
        l1.append(rem)

    length = len(l1)-1
    sum = 0
    for digit in l1:
        num = digit*(10**(length))
        sum += num
        (length) -= 1
    return sum


if x >= 0:
    out = rev(x)
    if out > 2147483647:
        print(0)
    else:
        print(out)
else:
    out = rev(-x)
    if out > 2147483648:
        print(0)
    else:
        print(-out)
