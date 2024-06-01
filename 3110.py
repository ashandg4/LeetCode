# Score of a String

s = "zaz"
count = 0
for i in range(len(s)-1):
    diff = abs(ord(s[i])-ord(s[i+1]))
    count += diff
print(count)
