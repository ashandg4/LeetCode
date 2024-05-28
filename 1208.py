# Get Equal Substrings Within Budget
s = "abcd"
t = "bcdf"
maxCost = 3

j = 0
for i in range(len(s)):
    maxCost -= abs(ord(s[i]) - ord(t[i]))
    if maxCost < 0:
        maxCost += abs(ord(s[j]) - ord(t[j]))
        j += 1
print(len(s)-j)
