# Maximum Height of a Triangle

red = 2
blue = 4


def f(a, b):
    ans = 0
    for i in range(100):
        if i % 2 == 0:
            if a >= (i+1):
                ans += 1
                a -= (i+1)
            else:
                return ans
        else:
            if b >= (i+1):
                ans += 1
                b -= (i+1)
            else:
                return ans


print(max(f(red, blue), f(blue, red)))
