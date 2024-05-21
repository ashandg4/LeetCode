# Palindrome Number

x = int(input("Enter a number: "))

if x < 0:
    print(False)
else:
    a = 0
    b = x
    while x > 0:
        a = a*10 + x % 10
        x //= 10
    print(a == b)
