# Count Pairs That Form a Complete Day II

hours = [12, 12, 30, 24, 24]

# remainder_freq = {}
# total_pairs = 0

# for time in hours:
#     remainder = time % 24
#     x = (24 - remainder) % 24

#     if x in remainder_freq:
#         total_pairs += remainder_freq[x]

#     remainder_freq[remainder] = remainder_freq.get(
#         remainder, 0) + 1

# print(total_pairs)


remainder_hours = [hour % 24 for hour in hours]

# Count frequencies of each remainder
remainder_freq = {}
for mod in remainder_hours:
    remainder_freq[mod] = remainder_freq.get(mod, 0) + 1

# Calculate the number of pairs
pairs = 0
# Pairs with both remainders 0
pairs += remainder_freq.get(0, 0) * (remainder_freq.get(0, 0) - 1) // 2
# Pairs with both remainders 12
pairs += remainder_freq.get(12, 0) * \
    (remainder_freq.get(12, 0) - 1) // 2
for i in range(1, 12):
    # Pairs with remainders i and 24-i
    pairs += remainder_freq.get(i, 0) * remainder_freq.get(24 - i, 0)

print(pairs)
