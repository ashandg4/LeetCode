# Replace Words

dictionary = ["a", "aa", "aaa", "aaaa"]
dict1 = sorted(dictionary)

sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
sent = sentence.split()

for word in range(len(sent)):
    txt = ""
    for char in sent[word]:
        txt += char
        if txt in dict1:
            sent[word] = txt
            break

print(" ".join(sent))
