# Reverse String

# Method-1
s = ['h', 'e', 'l', 'l', 'o']
# t = s.copy()
# for i in range(len(s)):
#     s[i] = t[-(i+1)]
# print(s)


# Method-2
l = 0
r = len(s) - 1

while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1
print(s)
