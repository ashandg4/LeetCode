# Number Complement

num = 5

bin_num = bin(num)[2:]
out = ''
for bit in bin_num:
    out += '1' if bit == '0' else '0'
print(int(out, 2))
