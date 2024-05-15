s = input("Enter a Roman numeral: ")
dict1={
    "M":1000,
    "D":500,
    "C":100,
    "L":50,
    "X":10,
    "V":5,
    "I":1,
}
count = 0
prev_value = 0

for char in s:
    value = dict1[char]
    count += value
    if value > prev_value:
        count -= 2 * prev_value
    prev_value = value

print("Integer: ",count)
