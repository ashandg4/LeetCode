# Longest Palindrome

s = "abccccdd"

letters = {}

for i in s:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1

count, odd = 0, 0

if len(letters) == 1:
    print(letters[s[0]])
else:
    for i in letters.values():
        if i > 1:
            if i % 2 == 0:
                count += i
            else:
                count += i-1
                odd += 1
        else:
            odd += 1

    if odd > 0:
        count += 1
    print(count)
