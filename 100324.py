# Clear Digits

def cleardig(s):
    lst = [x for x in s]
    while any(char.isdigit() for char in lst):
        for i, char in enumerate(lst):
            if char.isdigit():
                for j in range(i-1, -1, -1):
                    if not lst[j].isdigit():
                        del lst[i]
                        del lst[j]
                        break
                break
    return "".join(lst)


s = "cb34"
print(cleardig(s))
