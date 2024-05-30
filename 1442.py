# Count Triplets That Can Form Two Arrays of Equal XOR

arr = [2, 3, 1, 6, 7]
count = 0
xors = [0]
prefix = 0

for i, x in enumerate(arr):
    prefix ^= x
    xors.append(prefix)

for j in range(1, len(arr)):
    for i in range(0, j):
        xors_i = xors[j] ^ xors[i]
        for k in range(j, len(arr)):
            xors_k = xors[k + 1] ^ xors[j]
            if xors_i == xors_k:
                count += 1

print(count)
