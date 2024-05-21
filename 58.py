# Length of Last Word

s = "ashu anand   "
length = len(s) - 1

while length >= 0 and s[length] == ' ':
    length -= 1

# now length points to the last character of the last word
j = length

while j >= 0 and s[j] != ' ':       # Find the space before the start of the last word
    j -= 1

# The length of the last word is the difference between i and j
print(length-j)
