# Find Common Characters

words = ["cool", "lock", "cook"]

count = {}
result = []
chars = set(words[0])         # {'a','l','b','e'}

for char in chars:
    count[char] = words[0].count(char)
    # count={'b': 1, 'e': 1, 'a': 1, 'l': 2}


for word in words[1:]:
    for key in count.keys():
        if key not in word:
            count[key] = 0
        else:
            count[key] = min(count[key], word.count(key))

for key, value in count.items():
    result.extend([key] * value)
print(result)
